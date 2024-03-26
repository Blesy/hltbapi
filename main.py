from fastapi import FastAPI, __version__
from fastapi.staticfiles import StaticFiles
from howlongtobeatpy import HowLongToBeat

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/api/")
async def dataGame(id: int = 0):
    result = await HowLongToBeat().async_search_from_id(id)
    return result.__dict__