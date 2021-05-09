import kaggle_environments
import os

from kaggle_environments import make, evaluate, utils
env = make("hungry_geese", debug=True) #set debug to True to see agent internals each step

agent_path = "hungry-geese-local-set/agents/submission-ralph-coward.py"

if os.path.exists(agent_path):
    Agent = agent_path
else:
    raise Exception("Caminho do agente não existe")

env.reset()
agents = [Agent, Agent, Agent, Agent]
env.run(agents)


with open('./game.html','wb') as f:   # Use some reasonable temp name
    f.write(env.render(mode="html",width=700, height=600).encode("UTF-8"))

