# Next Steps Management System

## Purpose
This system manages project interruptions, tracks progress, and maintains continuity across work sessions.

## Project Structure

```
next-steps/
├── README.md                      # Documentation and overall structure
├── next-steps-index.md            # Index of all projects and dependencies
├── template.md                    # Template for new projects
├── active/                        # Currently being worked on
│   └── NNN-project-name/          # Active project (NNN = ID number)
│       ├── implementation-plan.md # Design document
│       ├── todo-list.md           # Tasks with checkboxes
│       ├── status.md              # Current state and context
│       ├── notes.md               # Optional: Future considerations
│       └── test-projects/         # Optional: For QA projects
│           └── testN-name/        # Individual test case (N = test number)
│               ├── todo-list.md   # Test-specific tasks
│               └── observations.md # Test results
├── paused/                        # Temporarily suspended projects
│   └── NNN-project-name/          # Same structure as active
├── completed/                     # Finished projects
│   └── NNN-project-name/          # Same structure as active
└── transition/                    # Checklists for state changes
    ├── activation-checklist.md    # Paused → Active
    ├── pausing-checklist.md       # Active → Paused
    └── completion-checklist.md    # Active → Completed
```

## Task Update Protocol
- **Mark tasks as complete immediately after execution** using `[x]` syntax
- Update todo-list.md before moving to the next task
- This ensures continuity if sessions are interrupted
- Example: 
  - Before: `- [ ] Review existing Next Steps README.md file`
  - After: `- [x] Review existing Next Steps README.md file`

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
