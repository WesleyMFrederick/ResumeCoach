# Implementation Plan for Naming Convention Refactoring

After analyzing the ResumeCoach codebase, I've identified numerous inconsistencies with the new style guide. Here's my proposed implementation plan:

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

## Phase 4: Testing and Validation

1. **Run unit tests** if available
2. **Manual testing** of key workflows:
   - Job description analysis
   - Resume generation
   - Any other core features

## Phase 5: Update Path References in Output Code

1. **Update file path generation code** to use new directory and file names:
   - References to `data/job_descriptions/`
   - References to `data/description_analyses/`
   - Other path references in the codebase

## Phase 6: Documentation

1. **Update any documentation** that references files, classes, or methods by name
2. **Create migration notes** for other developers

## Implementation Strategy

To minimize disruption, I recommend:

1. **Small, focused commits** - Group related changes (e.g., directory renames, then file renames)
2. **Regular testing** - Test after each significant change
3. **Coordinate with team** - Ensure everyone knows when these changes are happening
