import asyncio


async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("world")


async def hello_async():
    print("Hello, async world!")
    await asyncio.sleep(1)


async def background_task():
    print("Start background task")
    await asyncio.sleep(2)
    print("Finished background task")


async def create_back():
    task = asyncio.create_task(background_task())
    await task  # Ожидаем завершения задачи


async def fetch_data():
    await asyncio.sleep(1)
    return "data"


async def process_data():
    await asyncio.sleep(2)
    return "processed data"


async def test_gather():
    result1, result2 = await asyncio.gather(fetch_data(), process_data())
    print(result1, result2)
