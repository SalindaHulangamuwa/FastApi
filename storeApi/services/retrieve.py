
from storeApi.services.embeddingDocument import embed_documents
from storeApi.db.userDb import get_atlas_collection

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
    results = get_atlas_collection.aggregate(pipeline)
    array_of_results = []
    for doc in results:
        array_of_results.append(doc)
    return array_of_results