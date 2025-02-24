from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_documents(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    print(f"Splitting {len(documents)} documents into chunks of {chunk_size} characters")
    return text_splitter.split_documents(documents)