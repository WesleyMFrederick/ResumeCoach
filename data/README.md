# ResumeCoach Data Directory Structure

This directory contains all the data files used by the ResumeCoach application, organized into a structured hierarchy for clarity and maintainability.

## Directory Structure

```
data/
├── description_analyses/     # YAML outputs from job description analysis
├── prompt_templates/         # Prompt template files for LLM calls
├── user_files/               # Work experience, resume, and user data
├── job_descriptions/         # Job descriptions to analyze
├── tailored_work_experience/ # Generated files matching experience to job
├── tailored_resumes/         # Final generated resumes
└── resume_templates/         # Resume structure templates
```

## File Types

- **YAML files**: Structured data including job metadata, qualities, and user experience
- **Text files**: Job descriptions, resume content, and other unformatted data
- **Markdown files**: Prompt templates and documentation

## Naming Conventions

- Job description analysis files use the format: `{timestamp}_{company}_{position}_jobQualities.yaml`
- Job description source files should be named descriptively, e.g., `company_position_job_description.txt`
- User files should be clearly labeled, e.g., `Resume.txt`, `experience_company.yaml`
