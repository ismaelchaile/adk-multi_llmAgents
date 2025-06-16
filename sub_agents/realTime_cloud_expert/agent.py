from globalAgentsConfig import globalConfigs
cfg=globalConfigs()

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

realTime_cloud_expert_instance = LlmAgent(
    model=cfg['LLM_MODEL'],
    name='realTimeCloudExpert',
    description="""Answer real time questions using google_search tool, 
                    about about Google Cloud, Amazon Web Services and Azure
                """,
    instruction="""
        - Return a response from google_search tool, only if it is about pricing, 
        and real time info, for example status of cloud services.
        - Once you get the response, return to the root agent

    """,
    tools=[google_search]
)
