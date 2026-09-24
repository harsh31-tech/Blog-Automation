# MCP Blog Automation

An **MCP-powered blog writing automation** that combines **MCP resources, prompts, tools, and LLMs** to generate structured blogs from user-provided topics.

## Overview

This project demonstrates how the **Model Context Protocol (MCP)** can be used to build an automated blog-writing workflow.

Instead of sending a topic directly to an LLM, the system uses MCP to provide structured context such as:

- 📝 **Prompts** — Define how the blog should be generated
- 📚 **Resources** — Provide templates, instructions, and reference content
- 🔧 **Tools** — Perform actions required by the workflow
- 🤖 **LLM** — Generate the final blog using the provided context

### Workflow

```text
User Topic
    ↓
MCP Client
    ↓
Read MCP Resources
    ↓
Load Prompt / Instructions
    ↓
Call LLM
    ↓
Generate Structured Blog
    ↓
Final Markdown Output
```

## Features

- Generate blogs from a user-provided topic
- Read blog-writing instructions from Markdown resources
- Use reusable blog templates
- Combine MCP resources, prompts, and tools
- Integrate an LLM into the MCP workflow
- Generate structured Markdown content
- Demonstrate MCP client-server communication

## Tech Stack

- **Python**
- **FastMCP**
- **Model Context Protocol (MCP)**
- **LLM / OpenRouter**
- **Markdown**
- **uv** — Python package and project management

## Project Structure

```text
blog_automation/
│
├── src/
│   └── blog_automation/
│       │
│       ├── client/
│       │   └── client.py
│       │
│       ├── server/
│       │   └── server.py
│       │
│       └── resources/
│           ├── instructions.md
│           └── template.md
│
├── pyproject.toml
├── uv.lock
└── README.md
```

> Adjust the structure above if your current project folders differ.

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd blog_automation
```

### 2. Install dependencies

Make sure you have [uv](https://docs.astral.sh/uv/) installed.

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Do not commit your `.env` file to GitHub.

Add it to `.gitignore`:

```gitignore
.env
```

## Running the Project

Run the MCP client using:

```bash
uv run python src/blog_automation/client/client.py
```

The client connects to the MCP server, reads the required resources and prompts, and uses the configured LLM to generate the blog.

## Example

### Input

```text
Topic: What is Docker and why should developers use it?
```

### MCP Context

The system can load:

```text
instructions.md
template.md
```

The instructions define **how the content should be written**, while the template defines **how the final blog should be structured**.

### Output

```markdown
# What is Docker?

## Introduction

Docker is a platform that allows developers to...

## Why Use Docker?

- Consistent development environments
- Easier deployment
- Application isolation
- Reproducible environments

## How Docker Works

...

## Conclusion

...
```

## MCP Concepts Demonstrated

This project is primarily built as a learning project for understanding MCP.

### Resources

Resources provide contextual data to the LLM, such as:

```text
Blog instructions
Blog templates
Reference material
```

### Prompts

Prompts define reusable instructions for generating content.

For example:

```text
Generate a technical blog about the given topic using the provided
instructions and template.
```

### Tools

Tools allow the MCP server to expose executable functionality that the client or LLM can invoke.

### Client

The MCP client connects to the server and coordinates the workflow between MCP components and the LLM.

### Server

The MCP server exposes the project's resources, prompts, and tools through MCP.

## Learning Goals

This project is being built to understand:

- MCP architecture
- MCP servers and clients
- MCP resources
- MCP prompts
- MCP tools
- `stdio` communication
- LLM integration
- Context injection into LLM workflows
- Building practical MCP-powered applications

## Future Improvements

- [ ] Add multiple blog templates
- [ ] Add topic-specific research
- [ ] Add web-search capabilities
- [ ] Add blog quality evaluation
- [ ] Add automatic Markdown file generation
- [ ] Add blog metadata generation
- [ ] Add support for multiple LLM providers
- [ ] Add an HTTP-based MCP server
- [ ] Add automated publishing workflows

## License

This project is for learning and experimentation with **MCP, LLMs, and AI-powered automation**.
