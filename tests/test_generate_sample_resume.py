import unittest
from unittest.mock import MagicMock, patch
from flows.job_flow import GenerateSampleResume

class TestGenerateSampleResume(unittest.TestCase):
    def test_prep(self):
        # Create a mock shared dictionary
        shared = {
            "combined_yaml": {
                "metadata": {"Job Position Title": "Product Manager", "Company Name": "Acme Corp"},
                "qualities": [{"quality": "Leadership", "rank": 1}, {"quality": "Communication", "rank": 2}],
            },
            "job_unique_id": "1234567890_acme_product_manager",
        }

        # Create a GenerateSampleResume node
        generate_resume = GenerateSampleResume()

        # Call the prep method
        job_metadata, job_qualities, prompt_template, resume_template, job_unique_id = generate_resume.prep(shared)

        # Assert that the correct values are returned
        self.assertEqual(job_metadata, {"Job Position Title": "Product Manager", "Company Name": "Acme Corp"})
        self.assertEqual(len(job_qualities), 2)
        self.assertEqual(job_qualities[0]["quality"], "Leadership")
        self.assertIsInstance(prompt_template, str)
        self.assertIsInstance(resume_template, str)
        self.assertEqual(job_unique_id, "1234567890_acme_product_manager")

    @patch('flows.job_flow.call_llm')
    def test_exec(self, mock_call_llm):
        # Create mock inputs
        job_metadata = {"Job Position Title": "Product Manager", "Company Name": "Acme Corp"}
        job_qualities = [{"quality": "Leadership", "rank": 1}, {"quality": "Communication", "rank": 2}]
        prompt_template = "This is a test prompt with {jobMetadata} and {jobQualities}"
        resume_template = "This is a test resume template"
        job_unique_id = "1234567890_acme_product_manager"

        # Create a GenerateSampleResume node
        generate_resume = GenerateSampleResume()

        # Set the return value for the mock call_llm function
        mock_call_llm.return_value = "This is a sample resume"

        # Prepare the expected prompt
        expected_prompt = prompt_template.replace("{jobMetadata}", str(job_metadata)).replace("{jobQualities}", str(job_qualities))

        # Call the exec method
        sample_resume, unique_id = generate_resume.exec((job_metadata, job_qualities, prompt_template, resume_template, job_unique_id))

        # Assert that the correct values are returned
        self.assertEqual(sample_resume, "This is a sample resume")
        self.assertEqual(unique_id, "1234567890_acme_product_manager")

        # Assert that the call_llm function was called with the correct prompt
        mock_call_llm.assert_called_once_with(expected_prompt, model="gpt-4.5-preview")

if __name__ == "__main__":
    unittest.main()
