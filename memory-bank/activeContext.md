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
- Implemented the next-steps folder organization
- Refactored codebase to use underscore naming conventions

### Recent Technical Decisions
- Selected YAML as the structured data format for job qualities and metadata
- Implemented a structured organization system for the `memory-bank/next-steps` folder
- Implemented a shared memory pattern for flow state management
- Added timestamped unique IDs for job description processing
- Created validation logic to ensure consistent LLM outputs
- Organized data into specialized subdirectories for better project structure:
  - description_analyses/ for YAML outputs
  - prompt_templates/ for prompt files
  - user_files/ for Resume.txt and work experience
  - job_descriptions/ for job listings
  - Plus additional directories for future features
- Decided to enforce underscore naming conventions throughout the codebase

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

## Active Projects

### [002] Memory Bank Integration
- Started: 2025-03-13
- Activated: 2025-03-13
- Status: In progress
- Description: Integrating the Next Steps Management System with Cline's Memory Bank
- Current tasks:
  - Update custom instructions to reflect Next Steps system
  - Update Memory Bank files to align with Next Steps tracking
  - Test project creation and transition workflows

## Next Steps

1. Complete Active Project [002] Memory Bank Integration:
   - Update custom instructions with Next Steps Management System
   - Update `.clinerules` with Next Steps documentation
   - Update `activeContext.md` and `progress.md` with Active Projects sections
   - Ensure Memory Bank files properly reference Next Steps system

2. Additional Tasks:
   - Modify call to LLM model to include System Message
     - Break templates into system and user messages
   - Modify `tests/test_integration.py` to update the mock `call_llm` function 
   - Modify `flows/job_flow.py` to pass the `exc` argument to the `exec_fallback` method
   - Create remaining unit tests and implement automated integration testing
   - Implement mocking for the `call_llm` function to avoid using OpenAI credits
   - Modify `LoadJobDescription` to prevent duplicate checklist files
