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