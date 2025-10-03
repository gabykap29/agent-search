from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()

model_ollama = os.getenv("OLLAMA_MODEL")

llm_ollama = ChatOllama(
   model= model_ollama,
   temperature=0.2,
   max_token= 2048 
)
