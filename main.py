from fastapi import FastAPI, __version__
from howlongtobeatpy import HowLongToBeat

app = FastAPI()

@app.get("/api/")
async def dataGame(id: int = 0):
    result = await HowLongToBeat().async_search_from_id(id)
    return result.__dict__

@app.get("/api/{name}")
async def dataGame(name: str):
    result = await HowLongToBeat().async_search(name)
    return result.__dict__