import unittest
from unittest.mock import MagicMock
from flows.job_flow import LoadPromptTemplate
import os

class TestLoadPromptTemplate(unittest.TestCase):
    def test_prep(self):
        # Create a mock shared dictionary
        shared = {}

        # Create a LoadPromptTemplate node
        load_prompt = LoadPromptTemplate()

        # Call the prep method
        filepath = load_prompt.prep(shared)

        # Assert that the correct values are returned
        self.assertEqual(filepath, "data/prompt_templates/JobDescriptionTop10Attributes_prompt.md")

        # Create a mock shared dictionary with a prompt_template_file
        shared = {"prompt_template_file": "test_prompt_template.md"}

        # Call the prep method
        filepath = load_prompt.prep(shared)

        # Assert that the correct values are returned
        self.assertEqual(filepath, "test_prompt_template.md")

    def test_exec(self):
        # Create a LoadPromptTemplate node
        load_prompt = LoadPromptTemplate()

        # Create a mock file
        with open("test_prompt_template.md", "w") as f:
            f.write("This is a test prompt template.")

        # Call the exec method
        prompt_template = load_prompt.exec("test_prompt_template.md")

        # Assert that the correct values are returned
        self.assertEqual(prompt_template, "This is a test prompt template.")

        # Clean up the mock file
        os.remove("test_prompt_template.md")

    def test_post(self):
        # Create a mock shared dictionary
        shared = {}

        # Create a LoadPromptTemplate node
        load_prompt = LoadPromptTemplate()

        # Call the post method
        result = load_prompt.post(shared, None, "This is a test prompt template.")

        # Assert that the correct values are returned
        self.assertEqual(result, "default")
        self.assertEqual(shared["prompt_template"], "This is a test prompt template.")

if __name__ == "__main__":
    unittest.main()
