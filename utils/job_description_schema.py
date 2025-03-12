# utils/job_description_schema.py
import yaml
from utils.yaml_helpers import PreserveMarkdownLoader

def parse_yaml_from_llm_output(raw_output):
    """
    Extract and parse YAML content from LLM output while preserving markdown formatting.
    
    Args:
        raw_output (str): Raw text response from LLM
        
    Returns:
        dict/list: Parsed YAML content
    """
    # Check if the output is wrapped in ```yaml code blocks
    if raw_output.strip().startswith("```yaml") and "```" in raw_output[7:]:
        # Extract content between the yaml code blocks
        yaml_start = raw_output.find("```yaml") + 7
        yaml_end = raw_output.find("```", yaml_start)
        cleaned_output = raw_output[yaml_start:yaml_end].strip()
        print(f"Extracted YAML content from code blocks. Length: {len(cleaned_output)} chars")
    else:
        # If not wrapped in code blocks, use the original cleaning method
        cleaned_output = raw_output.strip().lstrip("'''yaml").rstrip("'''").strip()
        print(f"No code blocks found, using original cleaning. Length: {len(cleaned_output)} chars")
    
    return yaml.load(cleaned_output, Loader=PreserveMarkdownLoader)

def validate_job_yaml(parsed_yaml):
    """
    Validate the job description YAML structure with metadata and qualities.
    
    Args:
        parsed_yaml: The parsed YAML object
        
    Returns:
        dict: Validated YAML structure
        
    Raises:
        ValueError: If the YAML doesn't have the expected structure
    """
    if not isinstance(parsed_yaml, dict):
        raise ValueError("YAML is not a dictionary")
    
    # Validate metadata section
    if 'metadata' not in parsed_yaml:
        raise ValueError("Missing 'metadata' section")
    
    required_metadata = ['Company Name', 'Company About', 
                          'Job Position Title', 'Position Summary']
    for field in required_metadata:
        if field not in parsed_yaml['metadata']:
            raise ValueError(f"Missing metadata field: {field}")
    
    # Validate qualities section
    if 'qualities' not in parsed_yaml:
        raise ValueError("Missing 'qualities' section")
    
    if not isinstance(parsed_yaml['qualities'], list):
        raise ValueError("'qualities' should be a list")
    
    if len(parsed_yaml['qualities']) != 10:
        raise ValueError(f"Expected 10 qualities, found {len(parsed_yaml['qualities'])}")
    
    # Validate each quality
    for quality in parsed_yaml['qualities']:
        required_fields = ['quality', 'rank', 'reason', 'sentences']
        for field in required_fields:
            if field not in quality:
                raise ValueError(f"Quality missing required field: {field}")
    
    return parsed_yaml