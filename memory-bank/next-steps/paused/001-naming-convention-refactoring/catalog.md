# Naming Convention Catalog

## Directories (to rename)
- `data/job_descriptions` --> `data/job-descriptions`
- `data/description_analyses` --> `data/description-analyses`
- `data/prompt_templates` --> `data/prompt-templates`
- `data/resume_templates` --> `data/resume-templates`
- `data/tailored_resumes` --> `data/tailored-resumes`
- `data/tailored_work_experience` --> `data/tailored-work-experience`
- `data/user_files` --> `data/user-files`

## Other Directories
- `flows`
- `knowledge-base`
- `logs`
- `memory-bank`
- `memory-bank/next-steps`
- `memory-bank/plans`
- `tests`
- `utils`

## Files (to rename)
- `flows/job_flow.py` --> `flows/job-flow.py`
- `utils/all_code.py` --> `utils/all-code.py`
- `utils/call_llm.py` --> `utils/call-llm.py`
- `utils/file_io.py` --> `utils/file-io.py`
- `utils/job_description_schema.py` --> `utils/job-description-schema.py`
- `utils/yaml_helpers.py` --> `utils/yaml-helpers.py`

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
- `docs/all_code.md`
- `docs/design.md`
- `docs/PocketFlow/PocketFlow.md`
- `docs/PocketFlow/SETUP.md`
- `docs/PocketFlow/docs/_config.yml`
- `docs/PocketFlow/docs/agent.md`
- `docs/PocketFlow/docs/apps.md`
- `docs/PocketFlow/docs/async.md`
- `docs/PocketFlow/docs/batch.md`
- `docs/PocketFlow/docs/communication.md`
- `docs/PocketFlow/docs/core_abstraction.md`
- `docs/PocketFlow/docs/decomp.md`
- `docs/PocketFlow/docs/essay.md`
- `docs/PocketFlow/docs/flow.md`
- `docs/PocketFlow/docs/guide.md`
- `docs/PocketFlow/docs/index.md`
- `docs/PocketFlow/docs/llm.md`
- `docs/PocketFlow/docs/mapreduce.md`
- `docs/PocketFlow/docs/memory.md`
- `docs/PocketFlow/docs/multi_agent.md`
- `docs/PocketFlow/docs/node.md`
- `docs/PocketFlow/docs/paradigm.md`
- `docs/PocketFlow/docs/parallel.md`
- `docs/PocketFlow/docs/preparation.md`
- `docs/PocketFlow/docs/rag.md`
- `docs/PocketFlow/docs/structure.md`
- `docs/PocketFlow/docs/tool.md`
- `docs/PocketFlow/docs/viz.md`

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
