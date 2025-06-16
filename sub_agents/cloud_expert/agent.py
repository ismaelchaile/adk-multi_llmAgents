from globalAgentsConfig import globalConfigs
cfg=globalConfigs()

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

cloud_expert_instance = LlmAgent(
    model=cfg['LLM_MODEL'],
    name='cloudExpert',
    description='You are a cloud expert, that answers questions to users about about Google Cloud, Amazon Web Services and Azure',
    instruction="""
        - Answer with the best of your knowledge
        - Once you get the response, return to the root agent
    """
)
