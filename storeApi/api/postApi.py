
from fastapi import HTTPException
from storeApi.models.post import UserPostIn


post_table = {}
comments_table={}


def find_post(post_id:int):
    return post_table.get(post_id)


async def create_post(post: UserPostIn):
    data=post.dict()
    last_record_id=len(post_table)
    new_post={**data,"id":last_record_id}
    post_table[last_record_id]=new_post
    return  new_post


async def get_all_post():
    return  list(post_table.values())


async def delete_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    del post_table[post_id]
    return  None


async def update_post(post_id: int, post: UserPostIn):
    post_to_update = find_post(post_id)
    if not post_to_update:
        raise HTTPException(status_code=404, detail="Post not found")
    data = post.dict()
    updated_post = {**data, "id": post_id}
    post_table[post_id] = updated_post
    return  updated_post

