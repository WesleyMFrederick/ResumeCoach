``` mermaid
flowchart TD
    classDef tallNode fill:#F8DE7E,stroke:#000,color:#111,stroke-width:0,padding:1em;
    classDef completeNode fill:#90EE90,stroke:#000,color:#111,stroke-width:0,padding:1em;
    classDef inProgressNode fill:#ADD8E6,stroke:#000,color:#111,stroke-width:0,padding:1em;
    classDef plannedNode fill:#F8DE7E,stroke:#000,color:#111,stroke-width:0,padding:1em;

    subgraph "E5: Future Enhancements [Planned]"
        subgraph "F5.2: Additional MVP Elements [Planned]"
            id521["7.2.1 - Incorporate remaining MVP plan items"]:::plannedNode
        end
        subgraph "F5.1: Brand Evolution [Planned]"
            id511["7.1.1 - Guide professional brand growth"]:::plannedNode
        end
    end

    subgraph "E4: Accomplishments Generation [Planned]"
        subgraph "F4.2: Success Stories [Planned]"
            id421["6.2.2.1 - Structure challenge-action-result format"]:::plannedNode
            id422["6.2.2.2 - Align stories with job qualities"]:::plannedNode
        end
        subgraph "F4.1: Key Achievements [Planned]"
            id411["6.1.2.1 - Extract high-impact metrics"]:::plannedNode
            id412["6.1.2.2 - Format for visibility"]:::plannedNode
        end
    end

    subgraph "E3: Work Experience Bullets [Planned]"
        subgraph "F3.2: Tailoring to Job Qualities [Planned]"
            id321["5.2.2.1.1 - Semantic matching analysis"]:::plannedNode
            id322["5.2.2.1.2 - Quality-to-Experience Matrix"]:::plannedNode
            id323["5.2.2.1.3 - Evidence weighting"]:::plannedNode
            id324["5.2.2.2 - Score experiences for highlights"]:::plannedNode
            id325["5.2.2.3 - Address gaps in qualities"]:::plannedNode
        end
        subgraph "F3.1: Bullet Point Crafting [Planned]"
            id311["5.1.2.1 - Generate verb+task+outcome structure"]:::plannedNode
            id312["5.1.2.2 - Include 60-80% quantifiable outcomes"]:::plannedNode
            id313["5.1.2.3 - Limit to 8 bullets per job"]:::plannedNode
            id314["5.1.2.4 - Prioritize recent/relevant jobs"]:::plannedNode
        end
    end

    subgraph "E2: User Experience Processing [In Progress]"
        subgraph "F2.2: LLM Editing [In Progress]"
            id221["4.2.2.2 - Create LLM prompt for raw YAML"]:::inProgressNode
            id222["4.2.2.3.1 - Improve active voice & verbs"]:::inProgressNode
            id223["4.2.2.3.2 - Increase conciseness"]:::inProgressNode
            id224["4.2.2.3.3 - Flag important elements"]:::inProgressNode
            id225["4.2.2.4 - Review & iterate with feedback"]:::inProgressNode
        end
        subgraph "F2.1: Raw Work History [In Progress]"
            id211["4.1.2.1 - Manual YAML file editing"]:::inProgressNode
            id212["4.1.2.2 - Capture comprehensive details"]:::inProgressNode
        end
    end

    subgraph "E1: Job Description Analysis [Partially Complete]"
        subgraph "F1.2: Ideal Resume Generation [Planned]"
            id121["3.2.2.1 - Create prompt with metadata"]:::plannedNode
            id122["3.2.2.2 - Generate sample with formatting"]:::plannedNode
            id123["3.2.2.3 - Include top quality examples"]:::plannedNode
            id124["3.2.2.4 - Store for later comparison"]:::plannedNode
        end
        subgraph "F1.1: Metadata & Qualities Extraction [Complete]"
            id111["3.1.2.1 - Ingest job description md file"]:::completeNode
            id112["3.1.2.2 - Insert into ChatGPT 4o prompt"]:::completeNode
            id113["3.1.2.3 - Return structured YAML data"]:::completeNode
            id114["3.1.2.4 - Output job metadata & top 10 qualities"]:::completeNode
        end
    end

    "F1.1: Metadata & Qualities Extraction [Complete]"-->"F1.2: Ideal Resume Generation [Planned]"
```