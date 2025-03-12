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

## Next Development Priorities

### Immediate Tasks
1. **Resume Parsing Implementation**
   - Create a flow for ingesting and structuring resume text
   - Develop components for extracting experience sections
   - Implement categorization of skills and qualifications

2. **Experience Matching Engine**
   - Design algorithms to match job requirements with candidate experiences
   - Develop scoring system for experience relevance
   - Create relevance ranking for resume sections

3. **Resume Generation Pipeline**
   - Implement bullet point optimization for relevant experiences
   - Develop resume assembly component
   - Create formatting and output options

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
