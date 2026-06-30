import os
from tavily import TavilyClient
from config.config import TAVILY_API_KEY
from langchain_core.tools import tool

@tool
def research_tool(query: str, search_depth: str = "advanced"):
    """Fetch the answer for research topic. """
    tavily = TavilyClient(api_key=TAVILY_API_KEY)
    # Executing the search
    response = tavily.search(
        query=query,
        search_depth=search_depth,
        max_results=5,
        include_answer=True
    )
    # Format the results cleanly for the agent
    context = f"Direct Answer: {response.get('answer', 'N/A')}\n\n"
    context += "Top Sources & Snippets:\n"
    for idx, result in enumerate(response.get("results", []), 1):
        context += f"[{idx}] URL: {result['url']}\nSnippet: {result['content']}\n\n"

    return context