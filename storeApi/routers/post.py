from fastapi import APIRouter, HTTPException
from storeApi.models.post import UserPost,UserPostIn,comment,commentIn,userPostWithComments

router=APIRouter()

post_table = {}
comments_table={}


def find_post(post_id:int):
    return post_table.get(post_id)


@router.post('/',response_model=UserPost,status_code=201)
async def create_post(post: UserPostIn):
    data=post.dict()
    last_record_id=len(post_table)
    new_post={**data,"id":last_record_id}
    post_table[last_record_id]=new_post
    return new_post


@router.get("/post" , response_model=list[UserPost])
async def get_all_post():
    return list(post_table.values())



@router.delete("/post/{post_id}", status_code=204)
async def delete_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    del post_table[post_id]
    return None


@router.put("/post/{post_id}", response_model=UserPost)
async def update_post(post_id: int, post: UserPostIn):
    post_to_update = find_post(post_id)
    if not post_to_update:
        raise HTTPException(status_code=404, detail="Post not found")
    data = post.dict()
    updated_post = {**data, "id": post_id}
    post_table[post_id] = updated_post
    return updated_post


     
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
