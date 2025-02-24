from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders.pdf import PDFPlumberLoader as PDFLoader

def load_documents():
    loader = DirectoryLoader(
        "storeApi/documents",
        glob="**/*.pdf",
        loader_cls=PDFLoader
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents")
    return documents



