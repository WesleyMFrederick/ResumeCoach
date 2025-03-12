from flows.job_flow import flow

def main():
    shared = {
        "job_description_file": "data/job_descriptions/academia_PM_job_description.text",
        "prompt_template_file": "data/prompt_templates/JobDescriptionTop10Attributes_prompt.md"
    }
    flow.run(shared)
    
    # Print a success message after the flow completes
    output_files = shared.get("output_files", [])
    if output_files:
        print("\nJob processing completed successfully!")
        print("Generated output files:")
        for file_path in output_files:
            print(f"- {file_path}")

if __name__ == "__main__":
    main()
