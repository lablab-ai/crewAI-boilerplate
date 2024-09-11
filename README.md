# crewAI Boilerplate

**Python Version:** 3.10+  
**Package Manager:** Poetry

## Introduction

This boilerplate provides a streamlined setup for working with the crewAI framework, allowing developers to quickly integrate AI-driven content creation features into their projects. It is designed to be flexible and extendable, enabling users to modify and customize the AI agents to perform a wide range of tasks beyond the default setup.

With minimal configuration, this boilerplate serves as a solid foundation for automating tasks like content creation, research, or any AI-driven process, making it ideal for developers, content marketers, and digital strategists. The initial setup is ready to go, and can be tailored to suit specific needs.

## Current Core Capabilities

- **Automated Research:** Gathers relevant, up-to-date information using advanced web scraping techniques through Firecrawl integration.
- **Intelligent Planning:** Creates a coherent and logical outline for content based on collected data.
- **AI-Powered Writing:** Utilizes OpenAI's GPT models to generate high-quality, structured text.
- **SEO Optimization:** Implements keyword optimization, meta description creation, and proper heading structure.
- **Customizable Agents:** Modify or extend the built-in AI agents to handle other tasks or processes, tailored to specific workflows.

## Getting Started

### Prerequisites

Ensure your development environment meets the following requirements:

- Python 3.10 or higher
- Poetry package manager
- API keys for OpenAI and Firecrawl services

### Installation

1. Clone the boilerplate repository:

    ```bash
    git clone https://github.com/yourusername/crewAI-Boilerplate.git
    cd crewAI-Boilerplate
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install Poetry:

    ```bash
    pip install poetry
    ```

4. Install dependencies:

    ```bash
    poetry install
    ```

### Configuration

1. Copy the `.env.example` file to `.env`:

    ```bash
    cp .env.example .env
    ```

2. Add your API credentials in the `.env` file:

    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
    FIRECRAWL_API_KEY=your_firecrawl_api_key_here
    ```

3. Modify the agent configurations and tasks in the `config/agents.yaml` and `config/tasks.yaml` files to suit your needs.

## Usage

Run the following command to initialize the framework:

```bash
poetry run crew-ai
```

This will launch the default setup, which includes content creation. To customize agents or tasks, edit the configuration files and re-run the command. You can extend this boilerplate to suit a variety of AI-driven workflows.

## Project Structure
```
crewAI-Boilerplate/
├── src/
│   └── crew_ai/
│       ├── config/
│       │   ├── agents.yaml    # Defines AI agent configurations
│       │   └── tasks.yaml     # Specifies tasks for AI agents
│       ├── tools/
│       ├── crew.py
│       └── main.py
├── tests/
├── docs/
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```
