from tavily import TavilyClient
from config.config import TAVILY_API_KEY
from langchain_core.tools import tool

@tool
def recon_tool(query: str, search_depth: str = "advanced"):
    """Fetch the answer for recon topic. """
    return ""