from fastapi import UploadFile
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.pdf import PDFPlumberLoader as PDFLoader

async def extract_text_pdf(file: UploadFile) -> str:
    file.file.seek(0)
    loader = PDFLoader(file.file)
    documents = loader.load()  
    text = ' '.join([doc.page_content for doc in documents])  
    return text

async def extract_text_docx(file: UploadFile) -> str:
    file.file.seek(0)  
    loader = Docx2txtLoader(file.file)
    documents = loader.load() 
    text = ' '.join([doc.page_content for doc in documents]) 
    return text