import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# LLM setup
base_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
