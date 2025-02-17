from pydantic import BaseModel

class UserPostIn(BaseModel):
    body: str

class UserPost(UserPostIn):
    id: int

class commentIn(BaseModel):
       body: str
       post_id: int
       
class comment(commentIn):
      id: int

class userPostWithComments(UserPost):
     comments: list[comment]



# sample response of userPostWithComments
# {
#         "post": {"id": 0, "body": "My post"},
#         "comments": [{
#             "id": 2,
#             "post_id": 0,
#             "body": "My comment"
#         }]
# }

     