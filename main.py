from fastapi import FastAPI, __version__
from howlongtobeatpy import HowLongToBeat

app = FastAPI()

@app.get("/api/")
async def dataGame(id: int = 0):
    result = await HowLongToBeat().async_search_from_id(id)
    return result.__dict__

@app.get("/api/name/{name}")
async def dataName(name: str = ""):
    print(name)
    result = await HowLongToBeat().async_search(name)
    if result is not None and len(result) > 0:
        best_element = max(result, key=lambda element: element.similarity)
    else:
        return {"error": "No game found."}
    return best_element.__dict__