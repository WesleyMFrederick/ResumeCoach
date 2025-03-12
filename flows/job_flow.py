from pocketflow import Node, Flow
from utils.file_io import read_file, write_file
from utils.call_llm import call_llm
from utils.yaml_helpers import format_yaml_with_markdown, format_yaml_readable
from utils.job_description_schema import parse_yaml_from_llm_output, validate_job_yaml
import os
import datetime

class LoadJobDescription(Node):
    def prep(self, shared):
        return shared.get("job_description_file", "data/job_descriptions/job_description.txt")

    def exec(self, filepath):
        return read_file(filepath)
    
    def _clean_string_for_filename(self, text):
        """
        Convert a string to a filename-friendly format:
        - Convert to lowercase
        - Replace spaces with underscores
        - Remove special characters
        - Limit length
        """
        import re
        # Remove special characters and convert spaces to underscores
        cleaned = re.sub(r'[^\w\s]', '', text).lower().replace(' ', '_')
        # Limit length to avoid too long filenames
        return cleaned[:30]

    def post(self, shared, prep_res, exec_res):
        shared["job_description"] = exec_res
        
        # Simplify ID by just using a timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        shared["timestamp"] = timestamp
        
        print(f"Generated timestamp: {timestamp}")
        return "default"


class LoadPromptTemplate(Node):
    def prep(self, shared):
        return shared.get("prompt_template_file", "data/prompt_templates/JobDescriptionTop10Attributes_prompt.md")

    def exec(self, filepath):
        return read_file(filepath)

    def post(self, shared, prep_res, exec_res):
        shared["prompt_template"] = exec_res
        return "default"


class InjectJobDescription(Node):
    def prep(self, shared):
        return shared["prompt_template"], shared["job_description"]

    def exec(self, inputs):
        template, jd_text = inputs
        return template.replace("<<JOB_DESCRIPTION>>", jd_text)

    def post(self, shared, prep_res, exec_res):
        shared["final_prompt"] = exec_res
        return "default"


class CallLLM(Node):
    def prep(self, shared):
        return shared["final_prompt"]

    def exec(self, prompt):
        return call_llm(prompt)

    def post(self, shared, prep_res, exec_res):
        shared["raw_llm_output"] = exec_res
        return "default"


class ValidateOrRetryYAML(Node):
    def prep(self, shared):
        return shared["raw_llm_output"], shared["timestamp"]

    def exec(self, inputs):
        raw_output, timestamp = inputs
        # Extract YAML content from LLM response
        parsed_yaml = parse_yaml_from_llm_output(raw_output)
        
        # Validate the combined YAML structure using our domain-specific validator
        validated_yaml = validate_job_yaml(parsed_yaml)
        
        return validated_yaml, timestamp

    def exec_fallback(self, shared, prep_res, exc):
        print(f"YAML validation failed: {exc}")
        # Return None to indicate failure, which will be handled in post()
        return None, shared["timestamp"]
    
    def _clean_string_for_filename(self, text):
        """
        Convert a string to a filename-friendly format:
        - Convert to lowercase
        - Replace spaces with underscores
        - Remove special characters
        - Limit length
        """
        import re
        # Remove special characters and convert spaces to underscores
        cleaned = re.sub(r'[^\w\s]', '', text).lower().replace(' ', '_')
        # Limit length to avoid too long filenames
        return cleaned[:30]

    def post(self, shared, prep_res, exec_res):
        if exec_res[0] is None:
            print("YAML validation failed. Re-running LLM.")
            return "retry_llm"  # Follow the defined action in the flow
        
        validated_yaml, timestamp = exec_res
        
        # Store the validated combined YAML in shared
        shared["combined_yaml"] = validated_yaml
        
        # Now let's create a human-readable unique ID with company and position
        company_name = validated_yaml["metadata"].get("Company Name", "unknown")
        job_title = validated_yaml["metadata"].get("Job Position Title", "unknown")
        
        # Clean strings for filename use
        company_clean = self._clean_string_for_filename(company_name)
        job_clean = self._clean_string_for_filename(job_title)
        
        # Simplified ID format: timestamp_company_position
        unique_id = f"{timestamp}_{company_clean}_{job_clean}"
        shared["job_unique_id"] = unique_id
        
        print(f"Created human-readable unique ID: {unique_id}")
        return "default"


class SaveYAMLFiles(Node):
    def prep(self, shared):
        # Get unique ID generated earlier
        unique_id = shared.get("job_unique_id", "unknown")
        
        # Create the output filenames with the human-readable unique ID
        qualities_file = f"data/description_analyses/{unique_id}_jobQualities.yaml"
        metadata_file = f"data/description_analyses/{unique_id}_jobMetadata.yaml"
        
        # Add filenames for human-readable versions
        readable_qualities_file = f"data/description_analyses/{unique_id}_jobQualities_readable.yaml"
        readable_metadata_file = f"data/description_analyses/{unique_id}_jobMetadata_readable.yaml"
        
        return (qualities_file, metadata_file, 
                readable_qualities_file, readable_metadata_file,
                shared["combined_yaml"])

    def exec(self, inputs):
        (qualities_file, metadata_file, 
         readable_qualities_file, readable_metadata_file, 
         combined_yaml) = inputs
        
        output_files = []
        
        # Save metadata files (both formats)
        if "metadata" in combined_yaml:
            # Machine-friendly format with preserved markdown formatting
            metadata_yaml = format_yaml_with_markdown(combined_yaml["metadata"])
            write_file(metadata_file, metadata_yaml)
            output_files.append(metadata_file)
            
            # Human-readable format without literal blocks
            readable_metadata = format_yaml_readable(combined_yaml["metadata"])
            write_file(readable_metadata_file, readable_metadata)
            output_files.append(readable_metadata_file)
        
        # Save qualities files (both formats)
        if "qualities" in combined_yaml:
            # Machine-friendly format with preserved markdown formatting
            qualities_yaml = format_yaml_with_markdown(combined_yaml["qualities"])
            write_file(qualities_file, qualities_yaml)
            output_files.append(qualities_file)
            
            # Human-readable format without literal blocks
            readable_qualities = format_yaml_readable(combined_yaml["qualities"])
            write_file(readable_qualities_file, readable_qualities)
            output_files.append(readable_qualities_file)
        
        return output_files

    def post(self, shared, prep_res, exec_res):
        for file_path in exec_res:
            file_name = os.path.basename(file_path)
            print(f"Saved {file_name}")
        
        # Store the path to both files in shared memory if needed later
        shared["output_files"] = exec_res
        return "end"


# Create node instances
load_jd = LoadJobDescription()
load_prompt = LoadPromptTemplate()
inject_jd = InjectJobDescription()
call = CallLLM()
validate_yaml = ValidateOrRetryYAML()
save_yaml = SaveYAMLFiles()

# Define flow connections
load_jd >> load_prompt >> inject_jd >> call >> validate_yaml >> save_yaml

# Add the retry path
validate_yaml - "retry_llm" >> call

# Create the flow with the starting node
flow = Flow(start=load_jd)
