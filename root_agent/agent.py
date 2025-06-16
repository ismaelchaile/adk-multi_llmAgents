from globalAgentsConfig import globalConfigs
cfg = globalConfigs()

#defining the sub agents
from google.adk.agents import LlmAgent #used in root agent
from google.adk.tools.agent_tool import AgentTool # used as a wrapper to use tools inside a sub agent
from sub_agents.realTime_cloud_expert.agent import realTime_cloud_expert_instance #LLM agent with ADK native tool (google_search) for real time
from sub_agents.cloud_expert import cloud_expert_instance #LLM agent for info responses (no real-time)
from sub_agents.developer_expert.agent import developer_expert_instance #raw LLM agent
from sub_agents.embedded_systems_expert.agent import embedded_systems_expert_instance #raw LLM agent

# Parent agent used as coordinator. Assigns to it sub_agents for specific user requests
root_agent = LlmAgent(
    name="multiAgentOrchestrator",
    model=cfg["LLM_MODEL"],
    description="""Orchestrates various sub-agents for different user intents.""",
    instruction="""
        - For non real-time info as services comparison, among others alike, use the
        cloudExpert sub agent 
        - For developer questions, fix code errors and write code, use the developerExpert sub agent
        - For the case of embedded systems questios, call the embeddedSystems_expert sub agent
        - For cloud real-time topics, as pricing, services status, among others alike,
        use the realTimeCloudExpert tool
    """,
    sub_agents=[ # Assign sub_agents here
        developer_expert_instance,
        cloud_expert_instance, 
        embedded_systems_expert_instance
    ],
    tools=[
        AgentTool(realTime_cloud_expert_instance), #THIS IS A SUB AGENT WITH A FUNCTION TOOL
                                                  #MUST BE WRAPPED USING AgentTool
    ]
)