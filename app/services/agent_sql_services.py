from utils.tools_sql import toolsSql
from core.agent import agent
from database.db import DB
from models.gemini import llm_gemini
from models.ollama import llm_ollama
from config.template import template
from dotenv import load_dotenv
import os

load_dotenv()
model = os.getenv("MODEL")
llm = ""

def agent_sql(query: str) -> str:
    if model == "OLLAMA":
        llm = llm_ollama
    else: 
        llm = llm_gemini
    tool = toolsSql(DB, llm)
    agentAI = agent(llm, tool, template)
    response = ""
    for step in agentAI.stream({"messages": [query]}, stream_mode="values"):
        message = step["messages"][-1]
        response = message.content
    return response
