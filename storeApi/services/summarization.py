from langchain_community.llms import Together
from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain, LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

together_api_key = os.getenv("TOGETHER_API_KEY")

llm = Together(
    model="togethercomputer/mistral-7b-instruct",
    temperature=0,
    together_api_key=together_api_key  
)

def create_map_reduce_chain():

    # Map step
    map_template = """The following is a chunk of text:
    {text}
    
    Summarize this chunk in one or two sentences:"""
    
    map_prompt = PromptTemplate.from_template(map_template)
    map_chain = LLMChain(llm=llm, prompt=map_prompt)

    # Reduce step
    reduce_template = """The following are summaries of text chunks:
    {context}
    
    Combine these summaries into a single, coherent summary:"""
    
    reduce_prompt = PromptTemplate.from_template(reduce_template)
    
    # Create reduce chain
    reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)
    
    # Create StuffDocumentsChain
    combine_documents_chain = StuffDocumentsChain(
        llm_chain=reduce_chain,
        document_variable_name="context"
    )

    # Create ReduceDocumentsChain
    reduce_documents_chain = ReduceDocumentsChain(
        combine_documents_chain=combine_documents_chain
    )

    # Create MapReduceDocumentsChain
    map_reduce_chain = MapReduceDocumentsChain(
        llm_chain=map_chain,
        reduce_documents_chain=reduce_documents_chain,
        document_variable_name="text",
        return_intermediate_steps=False
    )

    return map_reduce_chain