import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()


def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Add it to your environment or .env file.")

    model_name = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

    return ChatGroq(
        api_key=api_key,
        model=model_name,
        temperature=0,
    )
