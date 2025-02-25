from storeApi.services.loadData import load_documents
from storeApi.services.splitDocument import split_documents
from storeApi.services.embeddingDocument import embed_documents
from storeApi.db.atlasDb import get_atlas_collection


def vector_store():

    data=load_documents()
    docs=split_documents(data)
    all_contents = [doc.page_content for doc in docs]

    embeddings = embed_documents(all_contents)
    docs_to_insert = [{"text": text, "embedding": embedding} for text, embedding in zip(all_contents, embeddings)]


    print("Inserting documents into MongoDB Atlas...")
    collection = get_atlas_collection()
    print(collection)
    result = collection.insert_many(docs_to_insert)
    print("Documents inserted successfully")
    print(f"Inserted {len(result.inserted_ids)} documents")



if __name__ == "__main__":
    vector_store()

    

