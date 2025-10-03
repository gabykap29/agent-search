from langgraph.prebuilt import create_react_agent

def agent(model, tool, template):
    agent = create_react_agent(model, tool, prompt=template)
    return agent