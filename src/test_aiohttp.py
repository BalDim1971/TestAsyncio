import aiohttp
import asyncio


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def test_get():
    html = await fetch('http://python.org')
    print(html)


import json


async def post_json(url, json_data):
    async with aiohttp.ClientSession() as session:
        # Преобразуем данные в JSON формат
        headers = {'Content-Type': 'application/json'}
        async with session.post(url, data=json.dumps(json_data), headers=headers) as response:
            # Возвращаем текст ответа (для простоты), но может быть и response.json(), если ответ в формате JSON
            return await response.text()


async def test_post():
    url = "https://httpbin.org/post"
    data = {"key": "value", "hello": "world"}
    response_text = await post_json(url, data)
    print(response_text)


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        try:
            response = await session.get(url)
            data = await response.text()
            print(data)
        except aiohttp.ClientError as e:
            print(f"Ошибка запроса: {e}")
        except asyncio.TimeoutError:
            print("Тайм-аут запроса")
        finally:
            await session.close()


async def test_try():
    await fetch_data("<http://example.com>")


async def task1():
    await asyncio.sleep(1)
    raise ValueError("Ошибка в задаче 1")


async def task2():
    await asyncio.sleep(2)
    print("Задача 2 выполнена")


async def test_gather():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await asyncio.gather(t1, t2, return_exceptions=True)
