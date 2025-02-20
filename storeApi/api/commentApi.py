from  fastapi import HTTPException
from storeApi.api.postApi import find_post
from storeApi.models.post import commentIn


post_table = {}
comments_table={}



def create_comment(comment: commentIn):
    post = find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    data = comment.dict()  
    last_record_id = len(comments_table)
    new_comment = {**data, "id": last_record_id}
    comments_table[last_record_id] = new_comment
    return new_comment


def get_comments_on_post(post_id: int):
    return [
        comment for comment in comments_table.values() if comment["post_id"] == post_id
    ]

def get_post_with_comments(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {
        "post": post,
        "comments": get_comments_on_post(post_id),
    }
