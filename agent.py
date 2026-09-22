from google.adk.agents.llm_agent import Agent
# https://google.github.io/adk-docs/agents/models
root_agent = Agent(
    model='<FILL_IN_MODEL>',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
