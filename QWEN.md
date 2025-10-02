# LangGraph Agent Template - Project Context

## Project Overview

This is a comprehensive starter template for building intelligent agents with LangGraph. The repository provides a structured project layout, example implementations, and comprehensive documentation for creating stateful multi-actor applications powered by LLMs.

### Key Features
- **Multi-LLM Support**: Claude (Anthropic), GPT-4 (OpenAI), and Gemini (Google) integration patterns
- **Comprehensive CI/CD**: GitHub Actions workflows for testing, code review, and integration
- **Claude Code Integration**: Specialized agents for code review, architecture, and quality assessment
- **Development Tools**: Pre-configured with mypy, ruff, pytest, and Jupyter notebooks
- **Docker Support**: Ready for containerized deployment with docker-compose
- **Evaluation Framework**: Built-in agent evaluation and testing capabilities

## Project Structure

```
Langgraph_Agents_template/
├── .env.example              # Example environment variables
├── .gitignore
├── AGENTS.md                # LangGraph development principles
├── docker-compose.yml       # Docker services configuration
├── langgraph.json           # LangGraph CLI configuration
├── pyproject.toml           # Project dependencies and configuration
├── README.md                # Project overview and setup instructions
├── src/                     # Source code
│   └── MyAgent/
│       ├── agent.py         # Main agent implementation
│       ├── configuration.py # Agent configuration
│       ├── cron.py          # Cron job definitions
│       ├── prompts.py       # Prompt templates
│       ├── schemas.py       # Data schemas
│       ├── utils.py         # Utility functions
│       ├── eval/            # Evaluation components
│       ├── subagents/       # Subagent implementations
│       └── tools/           # Agent tools
│           ├── default/     # Default tools (e.g., email_tools.py)
│           └── plateform_ab # Platform AB testing tools
├── notebooks/               # Jupyter notebooks with examples
│   ├── agent.ipynb          # Main agent example notebook
│   ├── evaluation.ipynb     # Evaluation notebook
│   └── test_tools.py        # Test tools for evaluation
└── tests/                   # Test files
```

## Technology Stack

- **Python 3.12+**: Required Python version for the project
- **LangGraph**: Framework for building stateful multi-actor applications
- **LangChain**: Integration with various LLM providers
- **Docker**: Containerization for deployment
- **Jupyter Notebooks**: Interactive development and examples
- **UV**: Modern Python package manager and environment tool

## Setup and Installation

### Prerequisites
- Python 3.12+
- Multiple LLM API Keys (configure as needed):
  - OpenAI API key (for GPT models)
  - Anthropic API key (for Claude models)
  - Google API key (for Gemini models)
- LangSmith API key (optional but recommended for tracing)

### Installation Process

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Aamirshazad/LangGraph_Agents_template.git
   cd LangGraph_Agents_template
   ```

2. **Create and activate a virtual environment:**
   
   Recommended (using `uv` for environment management):
   ```sh
   pip install uv
   uv sync --extra dev
   uv run
   ```

   Alternative (standard venv + pip):
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .\\.venv\\Scripts\\activate  # Windows (PowerShell)
   python -m pip install --upgrade pip
   pip install -e .
   ```

3. **Configuration:**
   Create a `.env` file in the repository root (copy from example):
   ```sh
   cp .env.example .env
   ```
   
   Edit `.env` and set your keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   LANGSMITH_API_KEY=your_langsmith_api_key
   LANGSMITH_TRACING=true
   LANGSMITH_PROJECT="your-project-name"
   ```

## LangGraph CLI Commands

Install the CLI:
```sh
pip install langgraph-cli
```

Common commands:
- `langgraph dev` — Start a lightweight development server locally (no Docker required)
- `langgraph up` — Launch a LangGraph API server in a Docker container (requires Docker)
- `langgraph build -t my-agent-image` — Build a Docker image for the LangGraph API server
- `langgraph dockerfile` — Generate a Dockerfile for customizing image builds

## Key Dependencies

From `pyproject.toml`:
- `langchain-core>=0.3.59`
- `langchain-openai`
- `langgraph>=1.0.0a3`
- `langgraph-cli[inmem]`
- `google-api-python-client>=2.128.0`
- `python-dotenv`
- `jupyter`
- `pytest`

## Development Conventions

### LangGraph Development Principles

1. **Deployment-First Approach**: All LangGraph agents should be written for deployment unless otherwise specified.

2. **Never add checkpointer**: Unless explicitly requested by the user.

3. **Export compiled graph as `app`**: This is a required pattern for new LangGraph agents.

4. **Use prebuilt components when possible**: They are deployment-ready and well-tested.

5. **Model preference hierarchy**: Anthropic > OpenAI > Google

6. **Keep state minimal**: MessagesState usually sufficient

### Agent Creation Process

To add a new agent to the template:
1. Create a new package under `src/`, e.g. `src/my_new_agent/`
2. Add your agent code (e.g. `agent.py`), tools (a `tools/` package), prompts, and tests
3. Update `pyproject.toml` to include the new package in `tool.setuptools.packages` and `tool.setuptools.package-dir`
4. Add any new dependencies to `pyproject.toml` and install them in your environment

Keep agent logic modular so it's easy to reuse prompts, tools, and components.

### Tool Creation

Create tool functions inside your agent package under a `tools` directory. Use LangChain-style decorators where applicable. Register or import your tools from the agent entrypoint so the runtime can discover them.

### Quick Start

- Examples and demos are provided as Jupyter notebooks in the `notebooks/` directory (for example: `notebooks/agent.ipynb`)
- Start the notebook server and open the example to run a demo agent end-to-end

## Docker Services

The `docker-compose.yml` defines the following services:
- `langgraph-redis`: Redis for caching and message queuing
- `langgraph-postgres`: PostgreSQL database for persistent storage
- `langgraph-api`: Main LangGraph API service

## File Descriptions

- **`AGENTS.md`**: Contains LangGraph development principles and best practices
- **`CLAUDE.md`**: Anthropic-specific integration guidelines
- **`GEMINI.md`**: Google-specific integration guidelines
- **`langgraph.json`**: Configuration for LangGraph CLI with graph definitions
- **`agent.py`**: Main agent implementation using LangGraph
- **`tools/default/email_tools.py`**: Example of default tools implementation (search_files tool)

## Testing and Evaluation

The project includes an evaluation framework and test files in the `tests/` directory. The `evaluation.ipynb` notebook provides tools for agent evaluation.

## Contributing

Contributions are welcome. Suggested workflow:
- Fork the repository
- Create a feature branch
- Add tests and update documentation
- Open a pull request describing your changes