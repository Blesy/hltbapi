import asyncio
from howlongtobeatpy import HowLongToBeat


async def dataGame(id: int = 0):
    result = await HowLongToBeat().async_search_from_id(id)
    print(result)
    # print(result.__dict__)

async def dataName(name: str = ""):
    result = await HowLongToBeat().async_search(name)
    print(len(result))
    if result is not None and len(result) > 0:
        best_element = max(result, key=lambda element: element.similarity)
    print(best_element.__dict__)

asyncio.run(dataName("Final Fantasy VII Rebirth"))