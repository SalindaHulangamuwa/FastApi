from fastapi import APIRouter, HTTPException, Depends
from together import Together
from storeApi.models.summarize import TextInput, SummaryResponse
from dotenv import load_dotenv

import os

load_dotenv()

router = APIRouter()

summaryPost_table = {}


def find_summaryPost(post_id:int):
    return summaryPost_table.get(post_id)

client = Together(api_key=os.getenv('TOGETHER_API_KEY'))

@router.post("/summarize/")
async def summarize_text(input: TextInput):
    print("Received Input:", input)
    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates clear and concise summaries."},
                {"role": "user", "content": f"Please provide a detailed summary of the following text:\n\n{input.text}"}
            ],
            temperature=0.7,
            max_tokens=150
        )
        
        summary = response.choices[0].message.content
        return {"summary": summary}
    
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error generating summary: {str(e)}"
        )


async def get_summary(input: TextInput):
    try:
        summary_response = await summarize_text(input)
        summary = summary_response.get("summary", "")
        
        if not summary:
            raise HTTPException(status_code=500, detail="Failed to generate summary")
        
        print("Generated Summary:", summary) 
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/postSummary", response_model=SummaryResponse, status_code=201)
async def create_post_summary(input: TextInput, summary: str = Depends(get_summary)):
    if not summary:
        raise HTTPException(status_code=400, detail="Summary generation failed")
    
    last_record_id = len(summaryPost_table)
    new_post = {"id": last_record_id, "title": "Summarized Post", "content": summary}
    summaryPost_table[last_record_id] = new_post
    
    return new_post

@router.get("/", response_model=list[SummaryResponse])
async def get_all_posts():
    return list(summaryPost_table.values())
    

@router.delete("/postSummary/{post_id}", status_code=204)
async def deletePostSummary(post_id: int):
    post = find_summaryPost(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    del summaryPost_table[post_id]
    return None