from langchain_community.llms import Together
from langchain.chains import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from storeApi.models.summarize import TextInput
import os

load_dotenv()

together_api_key = os.getenv("TOGETHER_API_KEY")


def create_summarization_chain(documents):
    llm = Together(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1", 
        together_api_key=together_api_key,  
        temperature=0.7, 
        max_tokens=500,  
    )

    document_prompt = PromptTemplate(
    input_variables=["page_content"], template="{page_content}"
)

    document_variable_name = "context"

    prompt = ChatPromptTemplate.from_template("Summarize this content: {context}")

    llm_chain = LLMChain(llm=llm, prompt=prompt)

    chain = StuffDocumentsChain(
    llm_chain=llm_chain,
    document_prompt=document_prompt,
    document_variable_name=document_variable_name,
    )

    summaries = chain.invoke(documents)
    # summaries = TextInput(text=summaries)
    # print(type(summaries))

    return (summaries)
