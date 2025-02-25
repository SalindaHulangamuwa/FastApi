from langchain_community.llms import Together
from dotenv import load_dotenv
import os


def llm_together():

    load_dotenv()
    llm = Together(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        together_api_key=os.getenv("TOGETHER_API_KEY"),
        temperature=0.7,
        max_tokens=500,
    )
    return llm
