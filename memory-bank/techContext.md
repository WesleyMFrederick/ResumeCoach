# Technical Context: ResumeCoach

## Technology Stack

### Core Technologies
- **Python**: Primary implementation language
- **PocketFlow**: Framework for creating agent-based AI workflows with a minimalist (100-line) implementation
- **YAML**: Data interchange format for structured information (preferred over JSON for better handling of multiline text)

### AI API Services
- **OpenAI ChatGPT**: Used for analyzing job descriptions and generating tailored content
- **Anthropic Claude**: Alternative LLM for specific reasoning tasks
- **Google Gemini**: Additional AI service for specialized processing
- **OpenRouter**: Can switch between models easily

### Development Environment
- **VS Code**: Primary IDE with Cline AI integration
- **Git**: Version control system

### AI Tools
- **Claude Desktop**: Uses the chat interface. Has MCP integration. Can use latest Claude models
- **ChatGPT Web Interface**: Uses the chat interface. Can use latest OpenAI models
- **Git**: Version control system

## PocketFlow Framework

PocketFlow is a minimalist LLM framework (100 lines of code) that provides the core architecture for ResumeCoach. It offers several key capabilities:

### Core Abstractions
1. **Node**: The fundamental building block with three execution steps:
   - `prep(shared)`: Reads/preprocesses data from shared store
   - `exec(prep_res)`: Executes compute logic (typically LLM calls)
   - `post(shared, prep_res, exec_res)`: Updates shared store and returns action string

2. **Flow**: Orchestrates a graph of Nodes with action-based transitions
   - Supports default transitions (`node_a >> node_b`)
   - Supports named action transitions (`node_a - "action_name" >> node_b`)
   - Enables branching and conditional execution paths

3. **Communication**: Methods for sharing data between nodes
   - **Shared Store**: A global data structure accessible by all nodes
   - **Params**: Node-local configuration for identifiers or task-specific settings

4. **Batch Processing**: Specialized nodes for handling large inputs or multiple iterations
   - `BatchNode`: Processes items in an iterable one at a time
   - `BatchFlow`: Runs a Flow multiple times with different parameters

5. **Advanced Features**:
   - `AsyncNode` and `AsyncFlow`: For asynchronous operations
   - `AsyncParallelBatchNode` and `AsyncParallelBatchFlow`: For concurrent processing

### Design Patterns
1. **Structured Output**: Ensuring LLM responses follow specific formats (typically YAML)
2. **Workflow Decomposition**: Breaking complex tasks into manageable steps
3. **Map-Reduce**: For processing large documents or datasets
4. **RAG (Retrieval Augmented Generation)**: For context-aware LLM responses
5. **Chat Memory**: For managing conversation history and context
6. **Agent**: For dynamic decision-making based on context
7. **Multi-Agent**: For collaborative problem-solving between multiple LLM agents

## Development Setup

### Environment Requirements
- Python 3.9+ with required dependencies
- Access to API keys for chosen LLM providers
- PocketFlow framework installation

### Project Structure
```
ResumeCoach/
├── assets/                  # Static resources
├── cline_docs/              # Project documentation
├── data/                    # Input/output data storage
│   ├── job_descriptions/    # Sample and user job descriptions
│   └── resume_templates/    # Resume formatting templates
├── docs/                    # Technical documentation
│   └── PocketFlow/          # PocketFlow documentation
├── flows/                   # PocketFlow definitions
│   └── job_flow.py          # Main job analysis workflow
├── logs/                    # Execution logs
├── memory-bank/             # Cline memory persistence
├── utils/                   # Utility functions
│   ├── call_llm.py          # LLM API interaction
│   ├── file_io.py           # File handling utilities
│   ├── job_description_schema.py # Schema validation
│   └── yaml_helpers.py      # YAML formatting utilities
├── main.py                  # Application entry point
└── requirements.txt         # Dependencies
```

## Technical Dependencies

### External Dependencies
- **PyYAML**: YAML parsing and generation
- **OpenAI API Client**: For ChatGPT interactions
- **Anthropic API Client**: For Claude interactions
- **Google API Client**: For Gemini interactions
- **PocketFlow**: Agent orchestration framework

### Internal Dependencies
- **utils.call_llm**: Abstraction for LLM service calls
- **utils.file_io**: File operations wrapper
- **utils.job_description_schema**: YAML validation logic
- **utils.yaml_helpers**: YAML formatting utilities

## Development Best Practices

Based on PocketFlow guidelines, the project follows these best practices:

1. **Context Management**: Providing clear, relevant context to LLM agents rather than dumping entire files or histories

2. **Action Space Design**: Creating well-structured, unambiguous sets of actions with minimal overlap

3. **Task Decomposition**: Finding the optimal granularity—not too coarse (overwhelming for an LLM) or too granular (lacks context)

4. **Structured Output**: Using YAML for structured output due to its superior handling of multiline text and lack of escape requirements compared to JSON

5. **Fault Tolerance**: Implementing Node retries, validation, and fallback mechanisms for robust error handling

## Technical Constraints

### Performance Considerations
- **API Rate Limits**: LLM providers impose usage limits
- **Response Time**: User experience depends on LLM response speed
- **Parallelization**: Current implementation is primarily sequential, though PocketFlow does support async parallel processing

### Security and Privacy
- **API Key Management**: Requires secure handling of LLM API credentials
- **User Data Privacy**: Resume and job data must be handled according to privacy best practices
- **Data Retention**: Clear policies needed for storage of user-submitted content

### Scalability Factors
- **Multiple Users**: Current design focuses on single-user operation
- **Concurrent Processing**: Limited by sequential flow design
- **Input Size Limitations**: LLM context windows restrict maximum input size

## Integration Points

### Input Integration
- **Text Files**: Job descriptions and resumes ingested as text
- **YAML Files**: Structured data stored in YAML format
- **Command Line Interface**: Primary user interaction method

### Output Integration
- **YAML Files**: Structured analysis results
- **Text Files**: Generated resume content
- **Terminal Output**: Status and result summaries

## Technical Roadmap

### Short-term Enhancements
- Implement resume parsing component using BatchNode for large resume processing
- Add experience matching algorithm potentially using RAG pattern
- Develop resume generation module possibly using agent pattern for dynamic content generation

### Long-term Considerations
- Web interface for improved user experience
- Database integration for history and persistence
- Multi-user support with accounts and profiles
- Exploring PocketFlow's AsyncParallel features for performance optimization
