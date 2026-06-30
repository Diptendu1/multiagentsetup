from langchain.agents import create_agent
from tools.todoist_tools import add_task,get_task

def create_todoist_agent(llm):
    return create_agent(
        model = llm, 
        tools = [add_task, get_task],
        system_prompt = (
            "You are a todoist agent. You are able to access a todo list stored on Todoist.\n\n"
            "INSTRUCTIONS:\n"
            "- Assist only with todo list related tasks.\n"
            "- Make sure you use the tools that you have provided to you.\n"
            "- Once you have the todo list information, respond with the details and then indicate you are transferring back to the supervisor with the 'FINAL ANSWER'."
        ),
        name = "todoist_agent"
    )