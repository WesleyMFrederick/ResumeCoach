import unittest
from unittest.mock import MagicMock
from flows.job_flow import LoadJobDescription
import os

class TestLoadJobDescription(unittest.TestCase):
    def test_prep(self):
        # Create a mock shared dictionary
        shared = {}

        # Create a LoadJobDescription node
        load_jd = LoadJobDescription()

        # Call the prep method
        filepath = load_jd.prep(shared)

        # Assert that the correct values are returned
        self.assertEqual(filepath, "data/job_descriptions/job_description.txt")

        # Create a mock shared dictionary with a job_description_file
        shared = {"job_description_file": "test_job_description.txt"}

        # Call the prep method
        filepath = load_jd.prep(shared)

        # Assert that the correct values are returned
        self.assertEqual(filepath, "test_job_description.txt")

    def test_exec(self):
        # Create a LoadJobDescription node
        load_jd = LoadJobDescription()

        # Create a mock file
        with open("test_job_description.txt", "w") as f:
            f.write("This is a test job description.")

        # Call the exec method
        job_description = load_jd.exec("test_job_description.txt")

        # Assert that the correct values are returned
        self.assertEqual(job_description, "This is a test job description.")

        # Clean up the mock file
        os.remove("test_job_description.txt")

    def test_post(self):
        # Create a mock shared dictionary
        shared = {}

        # Create a LoadJobDescription node
        load_jd = LoadJobDescription()

        # Call the post method
        result = load_jd.post(shared, None, "This is a test job description.")

        # Assert that the correct values are returned
        self.assertEqual(result, "default")
        self.assertEqual(shared["job_description"], "This is a test job description.")
        self.assertIn("timestamp", shared)
        self.assertIn("checklist_file", shared)
        self.assertIn("job_name", shared)

        # Check if the checklist file is created
        checklist_file = shared["checklist_file"]
        self.assertTrue(os.path.exists(checklist_file))

        # Check the content of the checklist file
        with open(checklist_file, "r") as f:
            checklist = f.readlines()
        self.assertEqual(len(checklist), 3)
        self.assertEqual(checklist[0], "[ ] Job description loaded\n")
        self.assertEqual(checklist[1], "[ ] Qualities extracted\n")
        self.assertEqual(checklist[2], "[ ] Sample resume generated\n")

        # Clean up the checklist file
        os.remove(checklist_file)

    def test_post_existing_checklist(self):
        # Create a mock shared dictionary
        shared = {}

        # Create a LoadJobDescription node
        load_jd = LoadJobDescription()

        # Create a mock file
        checklist_file = "data/description_analyses/test_job_description_checklist.txt"
        shared["checklist_file"] = checklist_file
        with open(checklist_file, "w") as f:
            f.write("[ ] Job description loaded\n")
            f.write("[ ] Qualities extracted\n")
            f.write("[ ] Sample resume generated\n")

        # Call the post method
        result = load_jd.post(shared, None, "This is a test job description.")

        # Assert that the correct values are returned
        self.assertEqual(result, "default")
        self.assertEqual(shared["job_description"], "This is a test job description.")
        self.assertIn("timestamp", shared)
        self.assertIn("checklist_file", shared)
        self.assertIn("job_name", shared)

        # Check if the checklist file exists
        self.assertTrue(os.path.exists(checklist_file))

        # Check the content of the checklist file
        with open(checklist_file, "r") as f:
            checklist = f.readlines()
        self.assertEqual(len(checklist), 3)
        self.assertEqual(checklist[0], "[ ] Job description loaded\n")
        self.assertEqual(checklist[1], "[ ] Qualities extracted\n")
        self.assertEqual(checklist[2], "[ ] Sample resume generated\n")

        # Clean up the checklist file
        os.remove(checklist_file)

if __name__ == "__main__":
    unittest.main()
