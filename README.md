This is a begginer introduction to Google ADK.
Here you find multi LLM agents that work according to the routing of a orchestrator agent (root_agent)

Goals:
1) To provide you something functional you can 'play' with for learning ADK.
2) The tricky selection of the type of agents, so sometimes the LLM gets confused, due the agents topics could be considered sometimes near between each other, so they are all tech agents.
3) Prompts provided use self directed LLM routing and user directed routing for more deterministic behaviour.

Prompts provided are of two cases:
1) To show the automatic routing orchetrated by the LLM (sometimes could be not deterministic)
2) Launching the right agent for the user query, using the agent name in the prompt. More deterministic.

##Installation##
mkdir adk
cd adk
clone inside adk folder this repo
python3 -m venv .adk
pip install google-adk
source .adk/bin/activate
code .

Now VScode should be launched inside the adk virtual env. If you go to root_agent/agent.py open the file, you should see something at the bottom of the vscode screen as --> ('adk': venv)

Advice: with the current folders organization, all works using the adk command as shown next.
In case you want to run in debug, organize the folders differently and/or update launch.json accordingly, and/or organize the 

##Run in web:##
Inside adk folder run: 
adk web multi_llmAgents 

Open the url and in the left select the root_agent
Now you can send your requests

##Run in terminal:##
Inside the adk folder run: 
adk web multi_llmAgents/root_agent

Now you can send your requests

Disclaimer:
You use the code at your own responsibility.
All damages to you or third parties are under your responsibility.
The code is provided as shown.
The code is not production ready.

License:
Read the LICENSE.md file.

More docs:
Spanish: https://docs.google.com/document/d/1aFqF3QYYpYzS2i3LgViFfcd8es2T304cKYZ6xQ2Rr7E/edit?usp=drive_link
English: https://docs.google.com/document/d/1JtJpi43HHax_2WAHx_IFNe5sqZNyVMK6Zl8f0ASIrnM/edit?usp=drive_link

This solution needs more testing and improvements.
This work is not perfect, maybe there are some mistakes, but it is functional and enough for learning purposes.