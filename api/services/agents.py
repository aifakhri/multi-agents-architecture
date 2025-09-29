from langgraph.prebuilt import create_react_agent

from tools.search import web_search



def research_agent():
    agent_object = create_react_agent(
        model="openai:gpt-4.1",
        tools=[web_search],
        prompt=(
            "You are a research agent.\n\n"
            "INSTRUCTIONS:\n"
            "- Assist ONLY with research-related tasks, DO NOT do any math\n"
            "- After you're done with your tasks, respond to the supervisor directly\n"
            "- Respond ONLY with the results of your work, do NOT include ANY other text."          
        ),
        name="research_agent"
    )

    return agent_object