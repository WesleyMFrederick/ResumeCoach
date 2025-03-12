import unittest
from unittest.mock import MagicMock, patch
from flows.job_flow import ValidateOrRetryYAML
from utils.job_description_schema import parse_yaml_from_llm_output, validate_job_yaml

class TestValidateOrRetryYAML(unittest.TestCase):
    def test_prep(self):
        # Create a mock shared dictionary
        shared = {"raw_llm_output": "test raw llm output", "timestamp": "20231026120000"}

        # Create a ValidateOrRetryYAML node
        validate_yaml = ValidateOrRetryYAML()

        # Call the prep method
        raw_output, timestamp = validate_yaml.prep(shared)

        # Assert that the correct values are returned
        self.assertEqual(raw_output, "test raw llm output")
        self.assertEqual(timestamp, "20231026120000")

    @patch('flows.job_flow.parse_yaml_from_llm_output')
    @patch('flows.job_flow.validate_job_yaml')
    def test_exec(self, mock_validate_job_yaml, mock_parse_yaml_from_llm_output):
        # Create a ValidateOrRetryYAML node
        validate_yaml = ValidateOrRetryYAML()

        # Set the return values for the mock functions
        mock_parse_yaml_from_llm_output.return_value = {"metadata": {}, "qualities": []}
        mock_validate_job_yaml.return_value = {"metadata": {}, "qualities": []}

        # Call the exec method
        validated_yaml, timestamp = validate_yaml.exec(("test raw llm output", "20231026120000"))

        # Assert that the correct values are returned
        self.assertEqual(validated_yaml, {"metadata": {}, "qualities": []})
        self.assertEqual(timestamp, "20231026120000")

        # Assert that the mock functions were called with the correct arguments
        mock_parse_yaml_from_llm_output.assert_called_once_with("test raw llm output")
        mock_validate_job_yaml.assert_called_once_with({"metadata": {}, "qualities": []})

    def test_exec_fallback(self):
        # Create a mock shared dictionary
        shared = {"timestamp": "20231026120000"}

        # Create a ValidateOrRetryYAML node
        validate_yaml = ValidateOrRetryYAML()

        # Call the exec_fallback method
        validated_yaml, timestamp, exc = validate_yaml.exec_fallback(shared, None, Exception("Test exception"))

        # Assert that the correct values are returned
        self.assertEqual(validated_yaml, None)
        self.assertEqual(timestamp, "20231026120000")
        self.assertIsInstance(exc, Exception)

    def test_post(self):
        # Create a mock shared dictionary
        shared = {"checklist_file": "test_checklist.txt"}

        # Create a ValidateOrRetryYAML node
        validate_yaml = ValidateOrRetryYAML()

        # Create a mock file
        with open("test_checklist.txt", "w") as f:
            f.write("[ ] Job description loaded\n")
            f.write("[ ] Qualities extracted\n")
            f.write("[ ] Sample resume generated\n")

        # Call the post method
        result = validate_yaml.post(shared, None, ({"metadata": {}, "qualities": []}, "20231026120000"))

        # Assert that the correct values are returned
        self.assertEqual(result, "default")
        self.assertEqual(shared["combined_yaml"], {"metadata": {}, "qualities": []})

        # Check if the checklist file is updated
        with open("test_checklist.txt", "r") as f:
            checklist = f.readlines()
        self.assertEqual(checklist[1], "[X] Qualities extracted\n")

        # Clean up the mock file
        import os
        os.remove("test_checklist.txt")

if __name__ == "__main__":
    unittest.main()
