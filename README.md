# AI Scripts - AI Agent Examples

This repository contains working examples and exercises for building AI agents from scratch using OpenAI and LangChain.

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/satishmane-sam/AI-Scripts.git
cd AI-Scripts
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set API Key
```bash
# Windows
set OPENAI_API_KEY=your-api-key-here

# macOS/Linux
export OPENAI_API_KEY=your-api-key-here
```

### 4. Run Examples
```bash
python examples/01_simple_agent.py
python examples/02_agent_with_tools.py
python examples/03_react_agent.py
python examples/04_complete_agent.py
```

## Repository Structure

```
AI-Scripts/
├── examples/              # Working code examples
│   ├── 01_simple_agent.py
│   ├── 02_agent_with_tools.py
│   ├── 03_react_agent.py
│   └── 04_complete_agent.py
├── exercises/            # Practice exercises
│   ├── exercise_1.py
│   └── exercise_2.py
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Examples

### Example 1: Simple Agent
Basic OpenAI integration - your first AI agent.

### Example 2: Agent with Tools
Adding tools and capabilities to your agent.

### Example 3: ReAct Agent
Implementing the ReAct (Reasoning + Acting) pattern.

### Example 4: Complete Agent
Full-featured agent system with all components.

## Exercises

Practice what you've learned:
- **Exercise 1**: Build your first agent from scratch
- **Exercise 2**: Add custom tools to your agent

## Requirements

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- pip package manager

## Dependencies

- `openai` - OpenAI API client
- `langchain` - AI application framework
- `langchain-openai` - LangChain OpenAI integration

## Important

- Never commit your API key to this repository
- Use environment variables for API keys
- Follow OpenAI's usage policies

## Resources

- [OpenAI Documentation](https://platform.openai.com/docs)
- [LangChain Documentation](https://python.langchain.com/)

