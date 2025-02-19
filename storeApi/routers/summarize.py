from fastapi import HTTPException, APIRouter
from storeApi.services.inputHandle import input_handle
from storeApi.services.summarization import create_map_reduce_chain
from storeApi.models.summarize import TextInput
from storeApi.services.splitText import split_text_into_chunks

router = APIRouter()

@router.post("/summarize/")
async def summarize_post(input: TextInput):
    try:
        # Step 1: Handle input (extract text from file or use direct text input)
        text = await input_handle(input)

        # Step 2: Split the text into chunks
        chunks = split_text_into_chunks(text)

        # Step 3: Create the map-reduce summarization chain
        map_reduce_chain = create_map_reduce_chain()

        # Step 4: Run the map-reduce summarization
        final_summary = map_reduce_chain.invoke({"input_documents": chunks})

        return {"summary": final_summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))