from fastapi import APIRouter
from storeApi.models.post import UserPost,UserPostIn
from ..api.postApi import create_post,get_all_post,delete_post,update_post

router=APIRouter()

@router.post('/',response_model=UserPost,status_code=201)
async def create_post_endpoint(post: UserPostIn):
    return await create_post(post)


@router.get("/post" , response_model=list[UserPost])
async def get_all_post_endpoint():
    return await get_all_post()



@router.delete("/post/{post_id}", status_code=204)
async def delete_post_endpoint(post_id: int):
    return await delete_post(post_id)
    


@router.put("/post/{post_id}", response_model=UserPost)
async def update_post_endpoint(post_id: int, post: UserPostIn):
    return await update_post(post_id, post)


     
# @router.post("/comment", response_model=comment, status_code=201)
# async def create_comment(comment: commentIn):
#     post = find_post(comment.post_id)
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")

#     data = comment.dict()  
#     last_record_id = len(comments_table)
#     new_comment = {**data, "id": last_record_id}
#     comments_table[last_record_id] = new_comment
#     return new_comment


# @router.get("/post/{post_id}/comment", response_model=list[comment])
# async def get_comments_on_post(post_id: int):
#     return [
#         comment for comment in comments_table.values() if comment["post_id"] == post_id
#     ]


# @router.get("/post/{post_id}", response_model=userPostWithComments)
# async def get_post_with_comments(post_id: int):
#     post = find_post(post_id)
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")

#     return {
#         "post": post,
#         "comments": await get_comments_on_post(post_id),
#     }
