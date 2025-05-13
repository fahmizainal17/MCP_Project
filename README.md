# MCP Project: Using MCP Server for Context Window Enhancement

This project demonstrates how to build and run an MCP (Model Context Protocol) server with tools, prompts, and resources to enhance the context window of an AI agent.

## 🧠 What is this project?

This is a minimal working example of how to implement an MCP server using [FastMCP](https://github.com/modelcontextprotocol/python-sdk). It provides:
- ✅ Tools (APIs that can be called by the AI agent)
- ✅ Resources (structured retrievable memory)
- ✅ Prompts (templates that condition the behavior of the agent)

It is designed to work with MCP-compatible agents to allow advanced interaction and better control over task execution.

---

## 🔁 Workflow Overview

1. `server.py` loads the MCP tools, prompts, and resources.
2. The AI agent (such as one in VSCode or a CLI tool) connects to the running MCP server.
3. The agent queries tools (e.g. for sentiment analysis), pulls in resources (e.g. user profiles), or injects prompt templates to control behavior.
4. Responses are returned in real time, improving how much context the agent can handle effectively.

---

## 🛠️ Tools

Tools are live APIs callable by the AI agent. They allow integration of logic into the AI context.

![Example Tool](image/example-tool.png)

---

## 📦 Resources

Resources are structured memory endpoints, like a profile store or cached documents.

![Example Resource](image/example-resource.png)

---

## ✨ Prompts

Prompts define the template or style of a specific instruction.

![Example Prompt](image/example-prompt.png)

---

## 🚀 How to Run

1. Make sure Python 3.10+ is installed.
2. (Optional) Create a virtual environment:

```bash
python3 -m venv venv_fahmi
source venv_fahmi/bin/activate
````

3. Install required dependencies:

```bash
pip install mcp textblob requests
python -m textblob.download_corpora
```

4. Run the MCP server:

```bash
python server.py
```

The MCP server will start and be available for connections from MCP-compatible tools like VSCode’s Copilot Labs or custom agents.

---

## 📁 File Structure

```
MCP_WORKSPACE/
├── MCP_Project/
│   ├── image/
│   │   ├── example-tool.png
│   │   ├── example-resource.png
│   │   └── example-prompt.png
│   ├── server.py
├── venv_fahmi/
└── README.md
```

---

## 🔗 References

* [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [Intro to MCP](https://www.youtube.com/watch?v=MjfaTE3apao)

