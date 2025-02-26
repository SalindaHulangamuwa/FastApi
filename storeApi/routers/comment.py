from fastapi import APIRouter
from storeApi.models.post import comment,commentIn,userPostWithComments
from ..api.commentApi import create_comment
from ..api.commentApi import get_post_with_comments,get_comments_on_post

router=APIRouter()

post_table = {}
comments_table={}



@router.post("/comment", response_model=comment, status_code=201)
async def create_comment_endpoint(comment: commentIn):
    return await create_comment(comment)

@router.get("/post/{post_id}/comment", response_model=list[comment])
async def get_comments_on_post_endpoint(post_id: int):
    return await get_comments_on_post(post_id)

@router.get("/post/{post_id}", response_model=userPostWithComments)
async def get_post_with_comments_endpoint(post_id: int):
    return await get_post_with_comments(post_id)

    
    


