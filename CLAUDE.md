# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **ticket automation system** built with LangGraph that routes incoming support tickets to specialized sub-agents based on query content. The system uses a router pattern to classify tickets and delegate them to domain-specific agents (company info, delivery, orders, transactions).

## Architecture

### Main Components

- **Router Agent** (`src/MyAgent/agent.py:agent`): Main LangGraph workflow that analyzes incoming messages and routes to appropriate sub-agents using structured output
- **State Management** (`src/MyAgent/schemas.py`): Defines `State` (extends MessagesState) and `RouterSchema` (Pydantic model for routing logic)
- **Sub-agents** (`src/MyAgent/subagents/`):
  - `company_info_agent.py`: Handles company/organization queries
  - `delivery_agent.py`: Manages delivery-related tickets
  - `order_agent.py`: Processes order information and updates
  - `transaction_agent.py`: Handles transaction inquiries
- **Tools** (`src/MyAgent/tools/`):
  - `db_tools/`: Database interaction tools and rag retrieval, and vector store management
  - `jira_tools/`: JIRA integration for ticket management


### Routing Flow

1. User message enters through `ticket_router_agent` (START node)
2. Router uses GPT-4.1 with structured output to classify query
3. Routes to one of four sub-agents based on classification
4. Sub-agents use specialized tools and return results

## Development Commands

### Environment Setup

```bash
# Recommended: using uv
pip install uv
uv sync --extra dev

# Alternative: standard venv
python3 -m venv .venv
.venv\Scripts\activate  # Windows
pip install -e .
```

### LangGraph CLI

```bash
# Install CLI
pip install langgraph-cli

# Development server (no Docker)
langgraph dev

# Docker deployment
langgraph up

# Build Docker image
langgraph build -t ticket-automation-image
```

### Testing

```bash
# Run all tests
pytest

# Run with parallelization
pytest -n auto

# Run specific test file
pytest tests/test_response.py

# Run notebooks validation
pytest tests/test_notebooks.py
```

### Code Quality

```bash
# Format and lint with ruff
ruff check .
ruff format .

# Type checking with mypy
mypy src/
```


## Key Implementation Details

- **Router uses structured output**: `llm.with_structured_output(RouterSchema)` for reliable routing
- **Command pattern**: Router returns `Command(goto=agent_name)` for state transitions
- **Sub-agents use create_agent**: All sub-agents built with `create_agent()` from langchain
- **Tools integration**: Each sub-agent has access to specific tools (e.g., order_agent uses `fetch_order_id`, `get_order_info`, `update_jira_ticket`)

## Important Notes

- Always write production-ready code using industry standards and best practices
- The router must return one of exactly four agents: `company_info_agent`, `delivery_agent`, `order_agent`, `transaction_agent`
- All agents share the same `State` schema which includes messages and router classification
- Tool imports may need fixing (e.g., `order_agent.py` references undefined tools that should be imported from tools modules)