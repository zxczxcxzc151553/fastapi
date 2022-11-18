from fastapi import FastAPI
from pydantic import Basemode1



app = FastAPI()


@app.get("/first/{id}")
async def root(id :int):
    return {"message": "Hello World", "id" : id}

@app.get("/second")
async def second(skip: int =0, limit: int =10):
    return {"skip": skip, "limit": limit}

@app.post("/cat")
async def cat():
    return ...