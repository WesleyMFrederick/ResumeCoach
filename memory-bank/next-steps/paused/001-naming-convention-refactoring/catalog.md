# Naming Convention Catalog

## Directories (properly named with underscores)
- `data/job_descriptions` 
- `data/description_analyses`
- `data/prompt_templates`
- `data/resume_templates`
- `data/tailored_resumes`
- `data/tailored_work_experience`
- `data/user_files`

## Other Directories
- `flows`
- `knowledge-base`
- `logs`
- `memory-bank`
- `memory-bank/next-steps`
- `memory-bank/plans`
- `tests`
- `utils`

## Files (properly named with underscores)
- `flows/job_flow.py`
- `utils/all_code.py`
- `utils/call_llm.py`
- `utils/file_io.py`
- `utils/job_description_schema.py`
- `utils/yaml_helpers.py`

## Other Files
- `flow.py`
- `main.py`
- `requirements.txt`
- `STYLE.md`
- `data/README.md`
- `data/description_analyses/20250312014354_academiaedu_senior_product_manager_jobMetadata_readable.yaml`
- `data/description_analyses/20250312014354_academiaedu_senior_product_manager_jobMetadata.yaml`
- `data/description_analyses/20250312014354_academiaedu_senior_product_manager_jobQualities_readable.yaml`
- `data/description_analyses/20250312014354_academiaedu_senior_product_manager_jobQualities.yaml`
- `data/description_analyses/20250312014354_academiaedu_senior_product_manager_sample-resume.txt`
- `data/description_analyses/20250312014354_checklist.txt`
- `data/description_analyses/academia_PM_job_description_checklist.txt`
- `data/description_analyses/job_description_checklist.txt`
- `data/job_descriptions/academia_PM_job_description.text`
- `data/job_descriptions/job_description.txt`
- `data/prompt_templates/craftPrompt.md`
- `data/prompt_templates/JobDescriptionTop10Attributes_prompt.md`
- `data/prompt_templates/prompt_jobDescriptionExtraction.md`
- `data/prompt_templates/prompt_JobDescriptionTop10Attributes.txt`
- `data/prompt_templates/prompt-job-description-sample-resume-template.md`
- `data/prompt_templates/prompt-job-description-sample-resume.md`
- `data/prompt_templates/reviseWorkExperience.md`
- `data/resume_templates/resume_template_text_prompt.md`
- `data/resume_templates/resume_template_text.txt`
- `data/tailored_resumes/`
- `data/tailored_work_experience/`
- `data/user_files/job_description_qualifications.yaml`
- `data/user_files/Resume.txt`
- `data/user_files/wmf_experience.yaml`

## Exempt Files and Directories
- All files in `docs/` directory (exempted from naming convention rules)

## flows/job_flow.py
### Classes
- `LoadJobDescription`
- `LoadPromptTemplate`
- `InjectJobDescription`
- `CallLLM`
- `ValidateOrRetryYAML`
- `SaveYAMLFiles`
- `GenerateSampleResume`
### Functions
- None
### Variables
- `load_jd`
- `load_prompt`
- `inject_jd`
- `call`
- `validate_yaml`
- `save_yaml`
- `generate_resume`
- `flow`

## main.py
### Classes
- None
### Functions
- `main`
### Variables
- None

## utils/all_code.py
### Classes
- None
### Functions
- `generate_directory_tree`
- `is_programming_file`
- `should_exclude`
- `should_include_file`
- `parse_arguments`
- `copy_to_clipboard`
- `main`
### Variables
- `FULL_CODE_FILE_NAME`
- `FILES_TO_INCLUDE`
- `PROGRAMMING_EXTENSIONS`
- `EXCLUDE_DIRS`
- `SCRIPT_NAME`
- `EXCLUDE_FILES`

## Test Cases
- Job description analysis:
  - Load job description from file
  - Extract qualities from job description using LLM
  - Validate extracted qualities
  - Save extracted qualities to YAML files
- Resume generation:
  - Load job description and extracted qualities
  - Generate sample resume using LLM
  - Save sample resume to file
