import os
from dotenv import load_dotenv
load_dotenv()

def globalConfigs():
    LLM_MODEL=os.getenv("LLM_MODEL") # for global use in all agents
    return  {
       "LLM_MODEL": LLM_MODEL
    }