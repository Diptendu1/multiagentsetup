from langchain.agents import create_agent
from tools.recommendation_tool import perform_gap_analysis, synthesize_intervention_card

def create_recommendation_agent(llm):
    return create_agent(
        model=llm,
        tools=[perform_gap_analysis, synthesize_intervention_card],
        system_prompt=(
            "You are an SME Strategy Agent. Use 'perform_gap_analysis' to identify the problem, then 'synthesize_intervention_card' to provide the solution."
            "Once you have a recommendation, Respond with the information and then indicate you are transferring back to the supervisor with the 'FINAL ANSWER'."
        ),
        name="research_agent"
    )