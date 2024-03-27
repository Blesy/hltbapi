import asyncio
from howlongtobeatpy import HowLongToBeat


async def dataGame(id: int = 0):
    result = await HowLongToBeat().async_search_from_id(id)
    print(result)
    # print(result.__dict__)

asyncio.run(dataGame(733110))