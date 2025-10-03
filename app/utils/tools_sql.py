from langchain_community.agent_toolkits import SQLDatabaseToolkit

def toolsSql(db, model):
    toolkit = SQLDatabaseToolkit(db=db, llm=model)
    return toolkit.get_tools()