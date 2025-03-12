# Active Context: ResumeCoach

## Current Work Focus

The ResumeCoach project is currently in the **Job Description Analysis Phase**. The primary focus is on extracting and structuring job description information to identify key qualifications and requirements for a position. This phase builds the foundation for subsequent resume matching and generation.

### Active Components
- Job description ingestion pipeline
- LLM-powered requirement extraction
- Structured YAML output generation
- Validation and error handling for LLM outputs

## Recent Changes

### Implemented Features
- Created the base PocketFlow architecture for the job description analysis workflow
- Developed a job description parsing flow with the following steps:
  - Loading job description text
  - Applying prompt templates
  - Calling LLM for analysis
  - Validating output structure
  - Generating structured YAML outputs
- Added error handling with retry logic for LLM calls
- Implemented human-readable and machine-readable output formats
- Restructured data directory with organized subdirectories
- Implemented the ability to select different models for different flows
- Implemented the Ideal Candidate Resume Generation node
- Implemented a failsafe mechanism to track progress and allow resuming interrupted workflows
- Added unit tests for the new node and the model selection functionality

### Recent Technical Decisions
- Selected YAML as the structured data format for job qualities and metadata
- Implemented a shared memory pattern for flow state management
- Added timestamped unique IDs for job description processing
- Created validation logic to ensure consistent LLM outputs
- Organized data into specialized subdirectories for better project structure:
  - description_analyses/ for YAML outputs
  - prompt_templates/ for prompt files
  - user_files/ for Resume.txt and work experience
  - job_descriptions/ for job listings
  - Plus additional directories for future features


### Technical Enhancements
- Refine error handling and recovery mechanisms
- Add comprehensive logging for debugging
- Implement unit tests for critical components

## Active Decisions and Considerations

### Design Questions
- How to structure the experience matching algorithm for optimal results?
- What format should the user provide their work experience in?
- How to balance automation with user control in resume generation?

### Implementation Concerns
- Ensuring LLM responses are consistently structured
- Managing LLM token usage and costs
- Handling edge cases in job description formats

### Research Areas
- Investigating best practices for resume optimization
- Exploring transfer learning techniques for experience matching
- Evaluating different prompt strategies for tailored results

## Next Steps

1.  Modify `tests/test_integration.py` to update the mock `call_llm` function to return a valid YAML string that includes the required "metadata" and "qualities" sections, and that can be parsed by the `validate_job_yaml` function.
2.  Modify `flows/job_flow.py` to pass the `exc` argument to the `exec_fallback` method.
3.  Create unit tests for the remaining nodes:
    *   LoadPromptTemplate
    *   InjectJobDescription
    *   CallLLM
    *   ValidateOrRetryYAML
    *   SaveYAMLFiles
    *   GenerateSampleResume
4.  Implement an automated integration test:
    *   Create a new test file (e.g., `tests/test_integration.py`).
    *   This test will:
        *   Create a mock job description file.
        *   Run the entire flow using the mock job description file.
        *   Assert that the correct files are created and that the checklist file contains the correct information.
5.  Mock the `call_llm` function to avoid using OpenAI credits:
    *   Use `unittest.mock.patch` to mock the `call_llm` function in the integration test.
    *   The mock function will return a predefined string.
6.  Modify `LoadJobDescription` to prevent duplicate checklist files:
    *   Modify the `LoadJobDescription` node to check if the checklist file already exists before creating it.
7.  Run all unit tests and the integration test.
