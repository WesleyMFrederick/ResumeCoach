
Before we do that, help me organize the next-steps folder.

# Objective
Work on the most relevant next step

## Context
- Next steps are stored in the next-steps folder
- Sometimes the current next-step project needs to be interrupted to work on a different issue
- We need a way to manage these next step sessions, plans, and tasks to deal with the situation when a new issue arises that needs to be addressed

## Example
We are currently working on a refactor project. However, I need to interupt that project to better organize the next steps folder. I still need to come back to the refactor project at a future date. I will need to re-analyze the refactor project based on any changes that occured since the plans were saved. In this case, we had to update the STYLE.md file in the root folder because we shouldn't be applying styles to 3rd party tools. This impacts the part where previously the plan was to update imports and references.

```
4. **Update imports and references**:
   - Fix all import statements to reflect new file names
   - Update all references to renamed files, classes, and functions
```

Another example, I want to add checkboxes to an plan that has steps. In the memory-bank/next-steps/naming-convention-catalog.md below, we wold want to show all the steps in Phase 1, 2, & 3 has being complete. For example:
- [x] **Create a refactoring branch** - Work in a separate branch to avoid disrupting the main codebase1.

```
## Phase 1: Preparation and Documentation

1. **Create a refactoring branch** - Work in a separate branch to avoid disrupting the main codebase
2. **Document current state** - Catalog all files, classes, functions, and variables that need renaming
3. **Set up test cases** - Ensure we have ways to verify functionality after refactoring

## Phase 2: Directory and File Renaming

1. **Rename directories**:
   - `data/job_descriptions` → `data/job-descriptions`
   - `data/description_analyses` → `data/description-analyses`
   - `data/prompt_templates` → `data/prompt-templates`
   - `data/resume_templates` → `data/resume-templates`
   - `data/tailored_resumes` → `data/tailored-resumes`
   - `data/tailored_work_experience` → `data/tailored-work-experience`
   - `data/user_files` → `data/user-files`

2. **Rename Python files**:
   - `flow.py` remains (single word)
   - `main.py` remains (single word)
   - `flows/job_flow.py` → `flows/job-flow.py`
   - `utils/all_code.py` → `utils/all-code.py`
   - `utils/call_llm.py` → `utils/call-llm.py`
   - `utils/file_io.py` → `utils/file-io.py`
   - `utils/job_description_schema.py` → `utils/job-description-schema.py`
   - `utils/yaml_helpers.py` → `utils/yaml-helpers.py`

## Phase 3: Code Content Refactoring

1. **Class renaming**:
   - `LoadJobDescription` → `load-job-description-node`
   - `LoadPromptTemplate` → `load-prompt-template-node`
   - `InjectJobDescription` → `inject-job-description-node`
   - `CallLLM` → `call-llm-node`
   - `ValidateOrRetryYAML` → `validate-or-retry-yaml-node`
   - `SaveYAMLFiles` → `save-yaml-files-node`
   - `GenerateSampleResume` → `generate-sample-resume-node`
   - `AnswerNode` → `answer-node`

2. **Function renaming**:
   - `_clean_string_for_filename` → `clean-string-for-filename`
   - Methods like `prep`, `exec`, `post`, `exec_fallback` should remain as is since they're predefined by the framework

3. **Variable renaming**:
   - `job_description` → `job-description`
   - `job_description_file` → `job-description-file`
   - `checklist_file` → `checklist-file`
   - `job_name` → `job-name`
   - `prompt_template` → `prompt-template`
   - `final_prompt` → `final-prompt`
   - `raw_llm_output` → `raw-llm-output`
   - Boolean variables to use appropriate prefixes: `is-valid`, `has-metadata`

4. **Update imports and references**:
   - Fix all import statements to reflect new file names
   - Update all references to renamed files, classes, and functions
```