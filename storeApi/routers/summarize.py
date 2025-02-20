from fastapi import HTTPException, APIRouter
from storeApi.services.inputHandle import input_handle
from storeApi.services.summarization import create_summarization_chain
from storeApi.models.summarize import TextInput
from storeApi.services.splitText import split_text_into_chunks
from langchain.schema import Document
from storeApi.routers.summaryApi import summarize_text

router = APIRouter()

@router.post("/summarize/")
async def summarize_post_endpoint(input: TextInput):
    try:
        text = await input_handle(input)
        if not text:
            raise ValueError("Input text is empty")

        chunks = split_text_into_chunks(text)
        if not chunks:
            raise ValueError("No chunks generated from the input text")

        documents = [Document(page_content=chunk) for chunk in chunks]

        stuff_chain = create_summarization_chain(documents)

        # type casting 
        summary_text = stuff_chain.get("output_text", "")

        if not summary_text:
            raise ValueError("No summary generated")
        
        text_input = TextInput(text=summary_text)

        result = summarize_text(text_input)
        return {"summary": result}

        # print(type(stuff_chain))

        # return {"summary": stuff_chain}
        # return summarize_text(stuff_chain)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))