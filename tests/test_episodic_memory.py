from memory.episodic import EpisodicMemory

memory = EpisodicMemory()

memory.add_episode(

    company="MSFT",

    query="Analyze Microsoft",

    tools_used=[
        "company_profile",
        "financial_data",
        "news_search",
        "sec_filings"
    ],

    status="Success"

)

print(memory.latest())

print()

print(memory.get_all())