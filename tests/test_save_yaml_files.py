import unittest
from unittest.mock import MagicMock, patch
from flows.job_flow import SaveYAMLFiles
import os

class TestSaveYAMLFiles(unittest.TestCase):
    def test_prep(self):
        # Create a mock shared dictionary
        shared = {
            "job_unique_id": "1234567890_acme_product_manager",
            "combined_yaml": {
                "metadata": {"Job Position Title": "Product Manager", "Company Name": "Acme Corp"},
                "qualities": [{"quality": "Leadership", "rank": 1}, {"quality": "Communication", "rank": 2}],
            }
        }

        # Create a SaveYAMLFiles node
        save_yaml = SaveYAMLFiles()

        # Call the prep method
        qualities_file, metadata_file, readable_qualities_file, readable_metadata_file, combined_yaml = save_yaml.prep(shared)

        # Assert that the correct values are returned
        self.assertEqual(qualities_file, "data/description_analyses/1234567890_acme_product_manager_jobQualities.yaml")
        self.assertEqual(metadata_file, "data/description_analyses/1234567890_acme_product_manager_jobMetadata.yaml")
        self.assertEqual(readable_qualities_file, "data/description_analyses/1234567890_acme_product_manager_jobQualities_readable.yaml")
        self.assertEqual(readable_metadata_file, "data/description_analyses/1234567890_acme_product_manager_jobMetadata_readable.yaml")
        self.assertEqual(combined_yaml, shared["combined_yaml"])

    @patch('flows.job_flow.write_file')
    @patch('flows.job_flow.format_yaml_with_markdown')
    @patch('flows.job_flow.format_yaml_readable')
    def test_exec(self, mock_format_yaml_readable, mock_format_yaml_with_markdown, mock_write_file):
        # Create mock inputs
        qualities_file = "data/description_analyses/1234567890_acme_product_manager_jobQualities.yaml"
        metadata_file = "data/description_analyses/1234567890_acme_product_manager_jobMetadata.yaml"
        readable_qualities_file = "data/description_analyses/1234567890_acme_product_manager_jobQualities_readable.yaml"
        readable_metadata_file = "data/description_analyses/1234567890_acme_product_manager_jobMetadata_readable.yaml"
        combined_yaml = {
            "metadata": {"Job Position Title": "Product Manager", "Company Name": "Acme Corp"},
            "qualities": [{"quality": "Leadership", "rank": 1}, {"quality": "Communication", "rank": 2}],
        }

        # Create a SaveYAMLFiles node
        save_yaml = SaveYAMLFiles()

        # Set the return values for the mock functions
        mock_format_yaml_with_markdown.return_value = "This is a formatted YAML with markdown"
        mock_format_yaml_readable.return_value = "This is a readable YAML"
        mock_write_file.return_value = None

        # Call the exec method
        output_files = save_yaml.exec((qualities_file, metadata_file, readable_qualities_file, readable_metadata_file, combined_yaml))

        # Assert that the correct values are returned
        self.assertEqual(output_files, [metadata_file, readable_metadata_file, qualities_file, readable_qualities_file])

        # Assert that the mock functions were called with the correct arguments
        mock_format_yaml_with_markdown.assert_called()
        mock_format_yaml_readable.assert_called()
        mock_write_file.assert_called()

    def test_post(self):
        # Create a mock shared dictionary
        shared = {}

        # Create a SaveYAMLFiles node
        save_yaml = SaveYAMLFiles()

        # Create mock inputs
        output_files = ["file1.yaml", "file2.yaml"]

        # Call the post method
        result = save_yaml.post(shared, None, output_files)

        # Assert that the correct values are returned
        self.assertEqual(result, "default")
        self.assertEqual(shared["output_files"], output_files)

if __name__ == "__main__":
    unittest.main()
