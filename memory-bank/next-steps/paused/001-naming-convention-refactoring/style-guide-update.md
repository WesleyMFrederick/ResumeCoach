# Style Guide Update Plan

## Rationale
Python's import system is incompatible with hyphenated module names. To maintain consistency and simplify development, we will use underscores throughout the codebase rather than hyphens.

## Changes Required
1. Update STYLE.md to specify underscore_naming instead of hyphen-naming
2. Remove all tasks related to converting underscores to hyphens
3. Check if any existing files or directories use hyphens that need conversion

## Draft STYLE.md Naming Conventions
### Files & Directories
- Use lowercase underscore format: `job_analysis_nodes.py`
- Group related files with consistent prefixes
- Collection files can use plural names: `templates.py`
- Directory names should be plural when containing multiple similar items: `flows/` for multiple flows
- Compound concept directories use underscores: `memory_bank/`, `knowledge_base/`
- Word "data" can be used as both singular and plural

### Classes
- Use lowercase underscore format: `validate_yaml_node`
- Standard suffixes: `_node`, `_service`, `_model`

### Functions
- Actions: `verb_object`: `extract_qualities`
- Getters: `get_noun`: `get_job_metadata`
- Utilities: `action_detail`: `clean_filename`

### Variables
- Basic: lowercase underscore: `job_description`
- Collections: plural nouns: `qualities`, `templates`
- Booleans: `is_*`, `has_*`: `is_valid`, `has_metadata`

## Implementation Notes
- This change simplifies implementation since most Python files already use underscores
- Ensures compatibility with Python's import system
- Follows standard Python conventions (PEP 8)
