# from langchain_community.llms import Together
# from langchain.chains import LLMChain
# from langchain.chains.combine_documents.stuff import StuffDocumentsChain
# from langchain.prompts import PromptTemplate
# from dotenv import load_dotenv
# from langchain_core.prompts import ChatPromptTemplate
# from langchain.prompts import PromptTemplate
# import os

# load_dotenv()

# together_api_key = os.getenv("TOGETHER_API_KEY")


# def create_summarization_chain(documents):
#     llm = Together(
#         model="mistralai/Mixtral-8x7B-Instruct-v0.1", 
#         together_api_key=together_api_key,  
#         temperature=0.7, 
#         max_tokens=500,  
#     )

#     document_prompt = PromptTemplate(
#     input_variables=["page_content"], template="{page_content}"
# )

#     document_variable_name = "context"

#     prompt = ChatPromptTemplate.from_template("Summarize this content: {context}")

#     llm_chain = LLMChain(llm=llm, prompt=prompt)

#     chain = StuffDocumentsChain(
#     llm_chain=llm_chain,
#     document_prompt=document_prompt,
#     document_variable_name=document_variable_name,
#     )

#     summaries = chain.invoke(documents)
#     # summaries = TextInput(text=summaries)
#     # print(type(summaries))

#     return (summaries)



from langchain_community.llms import Together
from langchain.chains import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

together_api_key = os.getenv("TOGETHER_API_KEY")

def create_summarization_chain(documents):

    llm = Together(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1", 
        together_api_key=together_api_key,  
        temperature=0.3, 
        max_tokens=500,  
    )

    document_prompt = PromptTemplate(
        input_variables=["page_content"], 
        template="{page_content}"
    )

    prompt = PromptTemplate.from_template(
    """
    Summarize the following content briefly and concisely. 
    Focus on the main ideas and avoid unnecessary details. 
    
    Example 1:
    Text: "In this study, we propose a novel deep learning approach for image classification. We train the model on a large dataset and achieve state-of-the-art accuracy."
    Summary: "A new deep learning model for image classification achieves high accuracy using a large dataset."
    
    Example 2:
    Text: "The research explores the impact of social media on mental health, finding that excessive use leads to anxiety and depression. The study suggests limiting usage to improve well-being."
    Summary: "Excessive social media use can cause anxiety and depression; limiting usage may improve mental health."
    
    Now summarize this content: {context}
    """
)


    llm_chain = LLMChain(llm=llm, prompt=prompt)

    chain = StuffDocumentsChain(
        llm_chain=llm_chain,
        document_prompt=document_prompt,
        document_variable_name="context", 
    )

    try:
      
        summaries = chain.invoke(documents)
        return summaries
    
    except Exception as e:

        print(f"An error occurred during summarization: {e}")
        return None


