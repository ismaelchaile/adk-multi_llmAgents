from globalAgentsConfig import globalConfigs
cfg=globalConfigs()


from google.adk.agents import LlmAgent

developer_expert_instance = LlmAgent(
    model=cfg["LLM_MODEL"],
    name='developerExpert',
    description='You are a python & javascript developer expert.Anwer questions only about those language, write code and fix errors in code',
    instruction="""
        - Generate code in the programming language the user ask
        - You do code review and fix errors
        - Answer whatever questions related to programming and software development.
        - Once you get the response, return to the root agent
    """,
)
