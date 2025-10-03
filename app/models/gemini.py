from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

gemini_model = os.getenv("GEMINI_MODEL")

llm_gemini = ChatGoogleGenerativeAI(
    model=gemini_model,
    temperature=0.5,
    max_tokens=2000,
)