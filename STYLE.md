# ResumeCoach Style Guide

## Purpose and Application

This style guide provides naming conventions and code structure guidelines for the ResumeCoach project. It ensures consistency and readability across the codebase, making it easier for developers to understand, maintain, and contribute to the project.

These guidelines should be applied to all new files and code created for the ResumeCoach project. Existing code should be refactored to adhere to these guidelines as time and resources permit.

## Required & Important Exceptions

The following elements are exempt from the style guide:

- Files and folders within the `memory-bank/` directory, including `.clinerules`, `activeContext.md`, `productContext.md`, `progress.md`, `projectbrief.md`, `systemPatterns.md`, and `techContext.md`. These files are managed by the Cline AI and have their own formatting conventions.
- Required Python files such as `__init__.py`.
- Third-party imports and their usage in the code.
- Files within the `docs/` directory, as these may include third-party documentation or have specific formatting requirements.
- Any files or folders that start with a dot (e.g., `.archive`, `.venv`).
- Only files created specifically for the ResumeCoach project should follow this style guide.

## Naming Conventions

### Files & Directories
- Use lowercase hyphenated format: `job-analysis-nodes.py`
- Group related files with consistent prefixes
- Collection files can use plural names: `templates.py`
- Directory names should be plural when containing multiple similar items: `flows/` for multiple flows
- Compound concept directories use hyphens: `memory-bank/`, `knowledge-base/`
- Word "data" can be used as both singular and plural

### Classes
- Use lowercase hyphenated format: `validate-yaml-node`
- Standard suffixes: `-node`, `-service`, `-model`

### Functions
- Actions: `verb-object`: `extract-qualities`
- Getters: `get-noun`: `get-job-metadata`
- Utilities: `action-detail`: `clean-filename`

### Variables
- Basic: lowercase hyphenated: `job-description`
- Collections: plural nouns: `qualities`, `templates`
- Booleans: `is-*`, `has-*`: `is-valid`, `has-metadata`

### Output Files
- Format: `{timestamp}-{entity-type}-{descriptor}.{extension}`
- Example: `20230501120000-job-analysis-qualities.yaml`

## Code Structure
- One class per file where possible
- Group related functionality in directories
- Place tests in parallel structure to implementation
