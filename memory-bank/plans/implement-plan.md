# ResumeCoach Implementation Plan

## 1. Overview
ResumeCoach is an agentic AI application that helps users tailor their resumes to specific job descriptions. The system ingests a job description, the user's work experience, and the current version of the user's resume. Through an iterative process of analysis and generation, the AI produces a tailored resume optimized for the target position.

## 2. Technology Stack

### 2.1 Core Technologies
* **Python**: Primary implementation language (2.1.1)
* **PocketFlow**: Framework for creating agent-based AI workflows with a minimalist implementation (2.1.2)
* **YAML**: Data interchange format for structured information (preferred over JSON for better handling of multiline text) (2.1.3)

### 2.2 AI API Services
* **OpenAI ChatGPT**: Used for analyzing job descriptions and generating tailored content (2.2.1)
* **Anthropic Claude**: Alternative LLM for specific reasoning tasks (2.2.2)
* **Google Gemini**: Additional AI service for specialized processing (2.2.3)
* **OpenRouter**: Can switch between models easily (2.2.4)

### 2.3 Development Environment
* **VS Code**: Primary IDE with Cline AI integration (2.3.1)
* **Git**: Version control system (2.3.2)

### 2.4 AI Tools
* **Claude Desktop**: Uses the chat interface with MCP integration (access to latest Claude models) (2.4.1)
* **ChatGPT Web Interface**: Uses the chat interface (access to latest OpenAI models) (2.4.2)

## 3. Epic 1: Job Description Analysis
Status: Feature 1.1 Completed

- Focuses on analyzing job descriptions
- LLM Extracts:
  - Job metadata
  - Exact quotes from the job description relevant to requirements, qualities, and skills
- LLM Synthesizes extracted data into top 10 requirements and qualities in structured YAML format
- LLM generates a sample resume that the perfect candidate would submit (for comparison in later steps)

### 3.1 Feature 1.1: Job Metadata & Qualities Extraction ✅
* **User Story:** "As a Product Manager user, I want the LLM to parse a job description so I can see a concise summary of the top 10 qualities the perfect candidate will possess." (3.1.1)
* **Implementation Details:** (3.1.2)
  * Python code that takes a job description markdown file (3.1.2.1)
  * Inserts into a prompt sent to the ChatGPT 4o model (3.1.2.2)
  * Returns structured YAML data in both concise format for LLMs and human-readable format (3.1.2.3)
    * Output includes Job Metadata and Job Top 10 Qualities with rankings and supporting sentences (3.1.2.4)

### 3.2 Feature 1.2: Ideal Candidate Resume Generation
* **User Story:** "As a Product Manager user, I want the LLM to generate a sample resume that the perfect candidate would submit so I can use it as a reference for my own resume tailoring." (3.2.1)
* **Implementation Details:** (3.2.2)
  * Create a prompt that uses the job description metadata and Top 10 Qualities (3.2.2.1)
  * Generate a sample text resume with properly formatted sections and bullet points (3.2.2.2)
  * Include examples of how the perfect candidate would demonstrate each of the top qualities (3.2.2.3)
  * Store the sample resume for comparison and reference in later steps (3.2.2.4)

## 4. Epic 2: User Experience Processing
Status: In Progress (Feature 2.1 started)

* Gathers raw work history, projects, situations, objectives, obstacles/challenges, actions/responsibilities, results/outcomes, tools, and skills (4.0.1)
* LLM edits raw work history for punch and clarity, preserving details for later steps (4.0.2)

### 4.1 Feature 2.1: Ingestion of Raw Work History
* **User Story:** "As a PM user, I want to input my past roles, responsibilities, outcomes, tools, and skills so the system can structure them for later use in resume tailoring." (4.1.1)
* **Implementation Details:** (4.1.2)
  * Currently using manual YAML file editing for work history input (4.1.2.1)
  * Format captures comprehensive details needed for later processing (4.1.2.2)

### 4.2 Feature 2.2: LLM-Based Editing for Punch & Clarity
* **User Story:** "As a PM user, I want the LLM to refine my raw work history for clarity and impact so I can form a strong, concise foundation for my resume." (4.2.1)
* **Implementation Details:** (4.2.2)
  * **Next Priority for Development** (4.2.2.1)
  * Create an LLM prompt that processes the raw YAML file (4.2.2.2)
  * Edit for clarity and punch while preserving all important details: (4.2.2.3)
    * Improve active voice and strengthen verbs (4.2.2.3.1)
    * Increase conciseness without losing detail (4.2.2.3.2)
    * Flag elements that could impact later iterations (4.2.2.3.3)
  * Review output and iterate with user feedback (4.2.2.4)
  * Initial development through copy/paste to refine prompt (4.2.2.5)

## 5. Epic 3: Work Experience Bullet Generation & Tailoring

* Takes the processed user experience artifacts and crafts tailored bullet points that match processed job qualities (5.0.1)

### 5.1 Feature 3.1: Bullet Point Crafting
* **User Story:** "As a PM user, I want the system to generate concise bullet points from my processed work experience so my resume highlights the most relevant responsibilities and outcomes." (5.1.1)
* **Implementation Details:** (5.1.2)
  * Generate bullets following structure: [Strong Action Verb, Past Tense] + [Task/Action/Responsibility] + [Outcome] (5.1.2.1)
  * Ensure 60-80% of bullets include quantifiable outcomes (5.1.2.2)
  * Limit to maximum 8 bullets per job (5.1.2.3)
  * Prioritize most recent job first, most relevant job second (5.1.2.4)

### 5.2 Feature 3.2: Tailoring to Top Job Qualities
* **User Story:** "As a PM user, I want each bullet point to align with the top job qualities identified in Epic 1 so my resume directly speaks to the job's key requirements." (5.2.1)
* **Implementation Details:** (5.2.2)
  * Implement combined matching approach: (5.2.2.1)
    * **Semantic Matching**: Use LLM to analyze semantic relationships between work experiences and job qualities (5.2.2.1.1)
    * **Quality-to-Experience Matrix**: Score each experience (0-5) against each quality (5.2.2.1.2)
    * **Evidence Weighting**: Boost scores for experiences with strong quantifiable outcomes (5.2.2.1.3)
  * Use final weighted scores to determine which experiences to highlight for each quality (5.2.2.2)
  * For remaining 20-40% of bullets, address any gaps between top job qualities and work experience (5.2.2.3)

## 6. Epic 4: Accomplishments Generation & Tailoring

* Expands beyond bullet points to highlight key achievements, success stories, and relevant metrics (6.0.1)

### 6.1 Feature 4.1: Key Achievement Summaries
* **User Story:** "As a PM user, I want to highlight my accomplishments and metrics so my resume quickly communicates the impact of my work." (6.1.1)
* **Implementation Details:** (6.1.2)
  * Extract and highlight highest-impact metrics and achievements (6.1.2.1)
  * Format for maximum visibility and impact (6.1.2.2)

### 6.2 Feature 4.2: Success Story Structuring
* **User Story:** "As a PM user, I want to present success stories clearly (challenges, actions, outcomes) so prospective employers see how I resolve obstacles and deliver results." (6.2.1)
* **Implementation Details:** (6.2.2)
  * Structure success stories in challenge-action-result format (6.2.2.1)
  * Align stories with top job qualities (6.2.2.2)

## 7. Epic 5: Future Enhancement Opportunities

* Additional items from the MVP plan that extend core functionality (7.0.1)

### 7.1 Feature 5.1: Long-Term Brand Evolution
* **User Story:** "As a PM user, I want guidance on how to evolve my professional brand so my career narrative continues to grow over time." (7.1.1)

### 7.2 Feature 5.2: Additional MVP Elements
* **User Story:** "As a PM user, I want to incorporate any remaining MVP plan items that don't neatly fit elsewhere so I can benefit from ongoing enhancements." (7.2.1)

## Next Steps

1.  Modify `tests/test_integration.py` to update the mock `call_llm` function to return a valid YAML string that includes the required "metadata" and "qualities" sections, and that can be parsed by the `validate_job_yaml` function.
2.  Modify `flows/job_flow.py` to pass the `exc` argument to the `exec_fallback` method.
3.  Create unit tests for the remaining nodes:
    *   LoadPromptTemplate
    *   InjectJobDescription
    *   CallLLM
    *   ValidateOrRetryYAML
    *   SaveYAMLFiles
    *   GenerateSampleResume
4.  Implement an automated integration test:
    *   Create a new test file (e.g., `tests/test_integration.py`).
    *   This test will:
        *   Create a mock job description file.
        *   Run the entire flow using the mock job description file.
        *   Assert that the correct files are created and that the checklist file contains the correct information.
5.  Mock the `call_llm` function to avoid using OpenAI credits:
    *   Use `unittest.mock.patch` to mock the `call_llm` function in the integration test.
    *   The mock function will return a predefined string.
6.  Modify `LoadJobDescription` to prevent duplicate checklist files:
    *   Modify the `LoadJobDescription` node to check if the checklist file already exists before creating it.
7.  Run all unit tests and the integration test.

# Plan Artifact
https://claude.site/artifacts/98ccac4d-8c1c-4777-843e-0b738a46c2ca
