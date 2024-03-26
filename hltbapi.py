from fastapi import FastAPI
from howlongtobeatpy import HowLongToBeat

app = FastAPI()

@app.get("/api/")
async def dataGame(id: int = 0):
    result = await HowLongToBeat().async_search_from_id(109434)
    return result.__dict__