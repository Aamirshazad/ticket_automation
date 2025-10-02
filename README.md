# LangGraph Agent Template

A comprehensive starter template for building intelligent agents with LangGraph. This repository provides a structured project layout, example implementations, and comprehensive documentation for creating stateful multi-actor applications powered by LLMs.

## Highlights

- **Multi-LLM Support**: Claude (Anthropic), GPT-4 (OpenAI), and Gemini (Google) integration patterns
- **Comprehensive CI/CD**: GitHub Actions workflows for testing, code review, and integration
- **Claude Code Integration**: Specialized agents for code review, architecture, and quality assessment
- **Development Tools**: Pre-configured with mypy, ruff, pytest, and Jupyter notebooks
- **Docker Support**: Ready for containerized deployment with docker-compose
- **Evaluation Framework**: Built-in agent evaluation and testing capabilities

## Requirements

- Python 3.12+ 
- **Multiple LLM API Keys** (configure as needed):
  - OpenAI API key (for GPT models)
  - Anthropic API key (for Claude models) 
  - Google API key (for Gemini models)
- LangSmith API key (optional but recommended for tracing)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Aamirshazad/LangGraph_Agents_template.git
   cd LangGraph_Agents_template
   ```

2. Create and activate a virtual environment.

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
   .\.venv\Scripts\activate  # Windows (PowerShell)
   python -m pip install --upgrade pip
   pip install -e .
   ```

3. Install development dependencies if needed:

   ```sh
   pip install -r requirements-dev.txt  # if present
   ```

## Configuration

Create a `.env` file in the repository root (you can copy the example):

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

## Quickstart / Running an Example

- Examples and demos are provided as Jupyter notebooks in the `notebooks/` directory (for example: `notebooks/agent.ipynb`).
- Start the notebook server and open the example to run a demo agent end-to-end.

## Creating a New Agent

To add a new agent to the template:

1. Create a new package under `src/`, e.g. `src/my_new_agent/`.
2. Add your agent code (e.g. `agent.py`), tools (a `tools/` package), prompts, and tests.
3. Update `pyproject.toml` to include the new package in `tool.setuptools.packages` and `tool.setuptools.package-dir`.
4. Add any new dependencies to `pyproject.toml` and install them in your environment.

Keep agent logic modular so it’s easy to reuse prompts, tools, and components.

## Adding Tools

Create tool functions inside your agent package under a `tools` directory. Use LangChain-style decorators where applicable.

Register or import your tools from the agent entrypoint so the runtime can discover them.

## LangGraph CLI (docker development & deployment)

Install the CLI:

```sh
pip install langgraph-cli
```

Common commands:

- `langgraph dev` — Start a lightweight development server locally (no Docker required).
- `langgraph up` — Launch a LangGraph API server in a Docker container (requires Docker).
- `langgraph build -t my-agent-image` — Build a Docker image for the LangGraph API server. 
- `langgraph dockerfile` — Generate a Dockerfile for customizing image builds.







## Contributing

Contributions are welcome. Suggested workflow:

- Fork the repository
- Create a feature branch
- Add tests and update documentation
- Open a pull request describing your changes

