
from storeApi.services.rag2.embeddingDocument import embed_documents
from storeApi.db.atlasDb import get_atlas_collection

def get_query_results(query):

    query_embedding = embed_documents(query)
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "queryVector": query_embedding,
                "path": "embedding",
                "exact": True,
                "limit": 5
            }
        }, {
            "$project": {
                "_id": 0,
                "text": 1
            }
        }
    ]
    collection=get_atlas_collection()
    results = collection.aggregate(pipeline)
    array_of_results = []
    for doc in results:
        array_of_results.append(doc)
    return array_of_results