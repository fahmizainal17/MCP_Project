"""
Simple MCP Server: Sentiment & Job Board Tool with Prompts and Resources

Overview:
---------
This MCP (Model Context Protocol) server registers a simple set of tools, resources, and prompts
for developers and agents. It provides basic NLP capabilities using TextBlob, as well as 
integration with an external job board API (Arbeitnow). The structure is built using the 
FastMCP class from the `mcp` SDK.

Purpose:
--------
- To analyze sentiment from any given text input.
- To fetch external job listings from a public job API.
- To simulate a resource retrieval system (user profiles).
- To define developer prompts for task execution and code review.

Workflow:
---------
1. **Tool: Sentiment Analysis**
   - Uses TextBlob to analyze input text.
   - Returns a polarity score (-1 to 1).

2. **Tool: Job Board API**
   - Makes a GET request to https://www.arbeitnow.com/api/job-board-api
   - Returns job listing data or an error message.

3. **Resource: get_profile**
   - Simulates retrieval of user profile data from a placeholder resource path.

4. **Prompt: dev_agent_prompt**
   - Provides instruction text for a developer agent to perform a task.

5. **Prompt: review_code**
   - Generates a review prompt for a block of source code.

How to Run:
-----------
- Run this script directly via `python server.py`.
- Tools and prompts become callable via the MCP protocol.
- This script must be run within an environment that has:
    - The `mcp` SDK installed
    - `textblob` and `requests` installed
    - Internet access for external API fetching

References:
-----------
- MCP SDK: https://github.com/modelcontextprotocol/python-sdk
- Tutorial: https://www.youtube.com/watch?v=MjfaTE3apao
"""


from mcp.server import FastMCP
from textblob import TextBlob
import requests

# Create a MCP server instance
mcp = FastMCP("Simple MCP")

def get_sentiment(text: str) -> float:
    """
    Analyze sentiment of the given text using TextBlob.
    
    Args:
        text (str): Input text to analyze.
    
    Returns:
        float: Polarity score between -1.0 and 1.0
               -1.0 = very negative
                0.0 = neutral
                1.0 = very positive
    """
    sentiment = TextBlob(text).sentiment
    return sentiment.polarity


# --------------------- Tools ---------------------

@mcp.tool()
def sentiment_analysis_api(text: str) -> float:
    """
    A sentiment analysis tool that uses TextBlob to determine the polarity of a given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        float: A polarity score ranging from -1.0 to 1.0.
               Negative = Negative sentiment,
               Zero = Neutral sentiment,
               Positive = Positive sentiment.
    """
    return get_sentiment(text)


@mcp.tool()
def access_job_board_api() -> dict:
    """
    Fetch job listings from the Arbeitnow public job board API.

    Returns:
        dict: A JSON dictionary of job listings if the request is successful.
              If unsuccessful, returns an error message as a string.
    """
    url = "https://www.arbeitnow.com/api/job-board-api"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Unable to fetch job listings. Reason: {str(e)}"}


# ------------------- Resources -------------------

@mcp.resource("profile:://{username}")
def get_profile(username: str) -> str:
    """
    Simulate retrieving a user profile from a database.

    Args:
        username (str): The username to retrieve the profile for.

    Returns:
        str: Placeholder profile info for the given username.
    """
    return f"Profile information for {username}"


# -------------------- Prompts --------------------

@mcp.prompt()
def dev_agent_prompt(task: str) -> str:
    """
    Developer agent prompt that instructs the agent to perform a task.

    Args:
        task (str): Description of the development task.

    Returns:
        str: Instructional prompt for the developer agent.
    """
    return f"You are a developer agent. Perform the following task: {task}"


@mcp.prompt()
def review_code(code: str) -> str:
    """
    Prompt for code review by an AI agent.

    Args:
        code (str): Source code to review.

    Returns:
        str: Prompt instructing to review the provided code.
    """
    return f"Please review the following code:\n\n{code}"


# -------------------- Main -----------------------

if __name__ == "__main__":
    mcp.run()
