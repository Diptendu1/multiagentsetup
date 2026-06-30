from langchain.agents import create_agent
from tools.recon_tool import recon_tool

def create_recon_agent(llm):
    return create_agent(
        model=llm,
        tools=[recon_tool],
        system_prompt=(
            "You are an expert Automated Financial Reconciliation Agent. "
            "Your task is to compare Internal Ledger Records against Bank Statements to spot discrepancies (missing entries, amount mismatches, or timing differences)."
            "Instructions:"
            "- Provide a clear breakdown of Matched Transactions, Discrepancies Found and Proposed Adjustments."
            "- Be precise with transaction IDs, dates, and currency values."
            "- Maintain a structured, professional ledger format using Markdown tables for readability."    
            "Once you have the research information, Respond with the information and then indicate you are transferring back to the supervisor with the 'FINAL ANSWER'."
        ),
        name="recon_agent"
    )