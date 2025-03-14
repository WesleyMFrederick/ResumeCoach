# Next Steps Management System

## Purpose
This system manages project interruptions, tracks progress, and maintains continuity across work sessions.

## Structure
- `/active` - Currently being worked on
- `/paused` - Temporarily suspended
- `/completed` - Finished projects
- `/transition` - Checklists for changing project states

## Project Files
Each project contains:
- `implementation-plan.md` - Design document
- `todo-list.md` - Tasks with checkboxes
- `status.md` - Current state, dependencies, and context

## Creating a New Project
1. Copy `template.md` to create project files
2. Place in `/active` with format: `NNN-project-name/`
3. Update `next-steps-index.md`

## Transitioning Projects
Follow checklists in `/transition` when:
- Pausing: Move from `/active` to `/paused`, following the pausing checklist
- Activating: Move from `/paused` to `/active`, following the activation checklist
- Completing: Move from `/active` to `/completed`, following the completion checklist

## Maintenance Guidelines
- Update timestamps when modifying files
- Maintain version history in `status.md`
- Document dependencies between projects
