from pymongo.operations import SearchIndexModel
from storeApi.db.atlasDb import get_atlas_collection
import time


collection = get_atlas_collection()

index_name = "vector_index"
search_index_model = SearchIndexModel(
    definition={
        "fields": [
            {
                "type": "vector",
                "numDimensions": 768,
                "path": "embedding",
                "similarity": "cosine"
            }
        ]
    },
    name=index_name,
    type="vectorSearch"
)
collection.create_search_index(model=search_index_model)

print("Polling to check if the index is ready. This may take up to a minute.")
predicate = None

if predicate is None:
    def predicate(index):
        return index.get("queryable") is True
while True:
    indices = list(collection.list_search_indexes(index_name))
    if len(indices) and predicate(indices[0]):
        break
    time.sleep(5)

print(index_name + " is ready for querying.")