from fastapi import FastAPI
from storeApi.routers.post import router as post_router
from storeApi.routers.comment import router as comment_router
app=FastAPI()

app.include_router(post_router, prefix="/posts")
app.include_router(comment_router, prefix="/comments")

