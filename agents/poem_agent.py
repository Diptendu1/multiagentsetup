from langchain.agents import create_agent

def create_poem_agent(llm):
    return create_agent(
        model=llm,
        tools = [],
        system_prompt = (
            "You are a poem agent.\n\n"
            "INSTRUCTIONS:\n"
            "- Write funny poems\n"
            "- Poems should not be more that 4 lines long\n"
        ),
        name = "poem_agent"
    )