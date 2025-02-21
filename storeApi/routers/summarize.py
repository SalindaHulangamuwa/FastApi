from fastapi import HTTPException, APIRouter, Depends
from storeApi.services.inputHandle import input_handle
from storeApi.services.summarization import create_summarization_chain
from storeApi.models.summarize import TextInput
from storeApi.services.token_utils import get_current_user
from langchain.schema import Document
# from storeApi.api.summaryApi import summarize_text, get_all_summaries

router = APIRouter()

@router.post("/")
async def summarize_post_endpoint(input: TextInput, current_user: str = Depends(get_current_user)):
    try:

        # if not current_user:
        #     raise HTTPException(status_code=401, detail="Unauthorized")
        
        text = await input_handle(input)
        
        if not text:
            raise ValueError("Input text is empty")

        # chunks = split_text_into_chunks(text)
        # if not chunks:
        #     raise ValueError("No chunks generated from the input text")

        # documents = [Document(page_content=chunk) for chunk in chunks]
        documents = [Document(page_content=text)]
        

        stuff_chain = create_summarization_chain(documents)

        # type casting 
        summary_text = stuff_chain

        if not summary_text:
            raise ValueError("No summary generated")
        
        # text_input = TextInput(text=summary_text)

        # result = summarize_text(text_input)
        return {"summary": summary_text}

        # print(type(stuff_chain))

        # return {"summary": stuff_chain}
        # return summarize_text(stuff_chain)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# @router.get("/summarize/",response_model=list[TextInput])
# async def get_all_summaries_endpoint():
#     return await get_all_summaries()

