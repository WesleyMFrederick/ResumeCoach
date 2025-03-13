Goal: Visualize the Implement plan in a mermaid chart
Actions:
* Use the mermaid template below
* **REQUIRED** - Follow % IMPORTANT LAYOUT NOTES instructions in template.
* **REQUIRED** - Shorten Epic, Feature, and Task Names to text in the display. Be Concise. Remove extra a, to, in, for, etc. 


```mermaid
flowchart TD
    % IMPORTANT COMMENT NOTES:
    % 1. The percentage sign (%) indicates a comment for the LLM
    % 2. The LLM MUST REMOVE all comments in its final output for Humans
    
    % IMPORTANT LAYOUT NOTES:
    % 1. Epics are defined in the CODE BOTTOM TO TOP but will DISPLAY LEFT-TO-RIGHT
    % 2. Features within each epic are defined in the CODE BOTTOM TO TOP but will DISPLAY LEFT-TO-RIGHT
    % 3. Nodes within features are defined in the code TOP-TO-BOTTOM will display TOP-TO-BOTTOM 


    % Custom node styling for better visibility
    classDef tallNode fill:#F8DE7E,stroke:#000,color:#111,stroke-width:0,padding:1em;

    % Epic Template Structure
    % {Importance Level}: Must Have, Should Have, Could Have, Nice to Have
    % {Status}: Planned, In Progress, Completed
    subgraph "E{EpicNumber}: {EpicTitle} [{Status}]"
        % Feature Subgraph - defined BOTTOM-UP for correct left-to-right display
        subgraph "F{EpicNumber}.{FeatureNumber}: {FeatureTitle} [{Status}]"
            % Nodes are written TOP-TO-BOTTOM and maintain that order
            % Use concise, descriptive task names
            % Include reference ID, short description
            % Add class for consistent styling
            id{EpicNumber}{FeatureNumber}{NodeNumber}["{ReferenceID} - {TaskDescription}"]:::tallNode
        end
    end

    % Additional Epic Subgraphs follow same pattern...
```

% Importance Level Framework:
% Must Have: Critical to project success, non-negotiable
% Should Have: Important but not critical, high priority
% Could Have: Beneficial but not necessary
% Nice to Have: Lowest priority, optional enhancements

% Example Filled Template
``` mermaid
flowchart TD
    classDef tallNode fill:#F8DE7E,stroke:#000,color:#111,stroke-width:0,padding:1em;

    
    subgraph "E2: Second Epic"
        subgraph "F2.2: Second Feature"
            id221["{implement-plan-id} - {Task Name Short}"]:::tallNode
        end
        subgraph "F2.1: First Feature"
            id211["{implement-plan-id} - {Task Name Short}"]:::tallNode
        end
    end
    subgraph "E1: Job Description Analysis"
        subgraph "F1.2: Sample Resume"
            id121["{implement-plan-id} - {Task Name Short}"]:::tallNode
            id122["{implement-plan-id} - {Task Name Short}" ]:::tallNode
            id123["{implement-plan-id} - {Task Name Short}"]:::tallNode
        end
        subgraph "F1.1: Extraction"
            id111["3.1.2.1 - Ingest .md file"]:::tallNode
            id112["3.1.2.2 - Insert .md into prompt. Send to 4o" ]:::tallNode
            id113["3.1.2.3 - Return YAML file. Top 10 qualities & supporting Sentences"]:::tallNode
        end
    end
```

% Recommended Best Practices:
% - Use clear, actionable task descriptions
% - Maintain consistent reference ID format
```