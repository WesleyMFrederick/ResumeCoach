# Next Steps Management System

## Purpose
This system manages project interruptions, tracks progress, and maintains continuity across work sessions. It relieves the anxiety of forgetting important context by ensuring all project information is documented in a structured, accessible format.

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
├── ideas/                         # Captured ideas not yet ready for implementation
│   └── idea-template.md           # Template for capturing new ideas
├── future/                        # Refined ideas ready for future implementation
│   └── future-template.md         # Template for future projects
└── transition/                    # Checklists for state changes
    ├── activation-checklist.md    # Paused → Active
    ├── pausing-checklist.md       # Active → Paused
    ├── completion-checklist.md    # Active → Completed
    ├── ideas-to-future-checklist.md # Ideas → Future
    └── future-to-active-checklist.md # Future → Active
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

## Capturing Ideas
1. Copy `idea-template.md` to create a new idea document
2. Fill in all relevant sections
3. Update `next-steps-index.md` Ideas section
4. For refinement, follow the ideas-to-future-checklist.md

## Transitioning Projects
Follow checklists in `/transition` when:
- Pausing: Move from `/active` to `/paused`, following the pausing checklist
- Activating: Move from `/paused` to `/active`, following the activation checklist
- Completing: Move from `/active` to `/completed`, following the completion checklist
- Refining Ideas: Move from `/ideas` to `/future`, following the ideas-to-future checklist
- Implementing Future Projects: Move from `/future` to `/active`, following the future-to-active checklist

## Maintenance Guidelines
- Update timestamps when modifying files
- Maintain version history in `status.md`
- Document dependencies between projects
- Document risks and future considerations for ideas and projects