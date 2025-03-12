import unittest
from unittest.mock import MagicMock
from flows.job_flow import InjectJobDescription

class TestInjectJobDescription(unittest.TestCase):
    def test_prep(self):
        # Create a mock shared dictionary
        shared = {"prompt_template": "test prompt template", "job_description": "test job description"}

        # Create a InjectJobDescription node
        inject_jd = InjectJobDescription()

        # Call the prep method
        template, jd_text = inject_jd.prep(shared)

        # Assert that the correct values are returned
        self.assertEqual(template, "test prompt template")
        self.assertEqual(jd_text, "test job description")

    def test_exec(self):
        # Create a InjectJobDescription node
        inject_jd = InjectJobDescription()

        # Call the exec method
        final_prompt = inject_jd.exec(("test prompt template <<JOB_DESCRIPTION>>", "test job description"))

        # Assert that the correct values are returned
        self.assertEqual(final_prompt, "test prompt template test job description")

    def test_post(self):
        # Create a mock shared dictionary
        shared = {}

        # Create a InjectJobDescription node
        inject_jd = InjectJobDescription()

        # Call the post method
        result = inject_jd.post(shared, None, "test final prompt")

        # Assert that the correct values are returned
        self.assertEqual(result, "default")
        self.assertEqual(shared["final_prompt"], "test final prompt")

if __name__ == "__main__":
    unittest.main()
