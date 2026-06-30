from langchain.agents import create_agent
from tools.research_tool import research_tool

def create_research_agent(llm):
    return create_agent(
        model=llm,
        tools=[research_tool],
        system_prompt=(
            "You are a professional Research Agent with access to a search engine. "
            "Your objective is to provide comprehensive, factual, and deeply analytical research report on the requested topic. "
            "Do not invent facts. Rely strictly on the search results provided. "
            "Structure your response with an Executive Summary, Key Findings, and a list of Source URLs used."
            "Once you have the research information, Respond with the information and then indicate you are transferring back to the supervisor with the 'FINAL ANSWER'."
        ),
        name="research_agent"
    )
