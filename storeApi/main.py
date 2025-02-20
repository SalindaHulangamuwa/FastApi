from fastapi import FastAPI
from storeApi.routers.post import router as post_router
from storeApi.routers.comment import router as comment_router
from storeApi.routers.summarize import router as summarize_router
from storeApi.routers.auth import router as auth_router

app=FastAPI()

app.include_router(post_router, prefix="/posts")
app.include_router(comment_router, prefix="/comments")
app.include_router(summarize_router, prefix="/summarizes")
app.include_router(auth_router, prefix="/auths")

