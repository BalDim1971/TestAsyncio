import asyncio
import aiohttp


async def fetch_weather(city):
    url = f"<http://api.weatherapi.com/v1/current.json?key=YOUR_KEY&q={city}>"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def weather_moscow():
    city = "Moscow"
    weather_data = await fetch_weather(city)
    print(f"Текущая температура в {city} составляет {weather_data['current']['temp_c']}°C")


async def display_weather_info(city):
    weather_data = await fetch_weather(city)
    temp_c = weather_data['current']['temp_c']
    condition = weather_data['current']['condition']['text']
    return f"В городе {city} сейчас {condition.lower()}, температура воздуха {temp_c}°C"

async def main_loop():
    cities = ["Moscow", "London", "New York"]
    tasks = [display_weather_info(city) for city in cities]
    weather_infos = await asyncio.gather(*tasks)
    for info in weather_infos:
        print(info)
