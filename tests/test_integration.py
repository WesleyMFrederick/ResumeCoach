import unittest
from unittest.mock import MagicMock, patch
from flows.job_flow import LoadJobDescription, LoadPromptTemplate, InjectJobDescription, CallLLM, ValidateOrRetryYAML, SaveYAMLFiles, GenerateSampleResume, Flow
import os

class TestIntegration(unittest.TestCase):
    @patch('flows.job_flow.call_llm')
    def test_integration(self, mock_call_llm):
        # Set the return value for the mock call_llm function
        mock_call_llm.return_value = """
metadata:
  Job Position Title: Test Job
  Company Name: Test Company
qualities:
  - quality: Leadership
    rank: 1
"""

        # Create a mock job description file
        job_description_file = "test_job_description.txt"
        with open(job_description_file, "w") as f:
            f.write("This is a test job description.")

        # Define the flow
        load_jd = LoadJobDescription()
        load_prompt = LoadPromptTemplate()
        inject_jd = InjectJobDescription()
        call = CallLLM()
        validate_yaml = ValidateOrRetryYAML()
        save_yaml = SaveYAMLFiles()
        generate_resume = GenerateSampleResume()

        load_jd >> load_prompt >> inject_jd >> call >> validate_yaml >> save_yaml >> generate_resume

        flow = Flow(start=load_jd)

        # Create a shared dictionary
        shared = {"job_description_file": job_description_file}

        # Run the flow
        try:
            flow.run(shared)
        except Exception as e:
            print(f"Exception during flow run: {e}")
            raise

        # Assert that the correct files are created
        job_name = "test_job_description"
        checklist_file = f"data/description_analyses/{job_name}_checklist.txt"
        qualities_file = f"data/description_analyses/{shared['job_unique_id']}_jobQualities.yaml"
        metadata_file = f"data/description_analyses/{shared['job_unique_id']}_jobMetadata.yaml"
        sample_resume_file = f"data/description_analyses/{shared['job_unique_id']}_sample-resume.txt"

        self.assertTrue(os.path.exists(checklist_file))
        self.assertTrue(os.path.exists(qualities_file))
        self.assertTrue(os.path.exists(metadata_file))
        self.assertTrue(os.path.exists(sample_resume_file))

        # Assert that the checklist file contains the correct information
        with open(checklist_file, "r") as f:
            checklist = f.readlines()
        self.assertEqual(len(checklist), 3)
        self.assertEqual(checklist[0], "[ ] Job description loaded\n")
        self.assertEqual(checklist[1], "[X] Qualities extracted\n")
        self.assertEqual(checklist[2], "[X] Sample resume generated\n")

        # Clean up the mock files
        os.remove(job_description_file)
        os.remove(checklist_file)
        os.remove(qualities_file)
        os.remove(metadata_file)
        os.remove(sample_resume_file)

if __name__ == "__main__":
    unittest.main()
