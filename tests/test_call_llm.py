import unittest
from unittest.mock import MagicMock, patch
from flows.job_flow import CallLLM
from utils.call_llm import call_llm

class TestCallLLM(unittest.TestCase):
    def test_prep(self):
        # Create a mock shared dictionary
        shared = {"final_prompt": "test final prompt"}

        # Create a CallLLM node
        call_llm_node = CallLLM()

        # Call the prep method
        prompt = call_llm_node.prep(shared)

        # Assert that the correct values are returned
        self.assertEqual(prompt, "test final prompt")

    @patch('flows.job_flow.call_llm')
    def test_exec(self, mock_call_llm):
        # Create a CallLLM node
        call_llm_node = CallLLM()

        # Set the return value for the mock call_llm function
        mock_call_llm.return_value = "This is a sample resume"

        # Call the exec method
        sample_resume = call_llm_node.exec("test final prompt")

        # Assert that the correct values are returned
        self.assertEqual(sample_resume, "This is a sample resume")

        # Assert that the call_llm function was called with the correct prompt
        mock_call_llm.assert_called_once_with("test final prompt")

    def test_post(self):
        # Create a mock shared dictionary
        shared = {}

        # Create a CallLLM node
        call_llm_node = CallLLM()

        # Call the post method
        result = call_llm_node.post(shared, None, "test raw llm output")

        # Assert that the correct values are returned
        self.assertEqual(result, "default")
        self.assertEqual(shared["raw_llm_output"], "test raw llm output")

if __name__ == "__main__":
    unittest.main()
