from globalAgentsConfig import globalConfigs
cfg=globalConfigs()

from google.adk.agents import LlmAgent

embedded_systems_expert_instance = LlmAgent(
    model=cfg['LLM_MODEL'],
    name='embeddedSystems_expert',
    description='You assist users with questions only about embedded systems and firmware',
    instruction="""
        - Answer the user questions to the best of your knowledge
        - Once you get the response, return to the root agent
    """
)
