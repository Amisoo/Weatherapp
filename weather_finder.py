from typing import List, Any

import python_weather

import asyncio
import os

data: list[Any] = []
forecast_weather = []


async def getweather(town: str):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(town)

        data.append(weather.current.temperature)
        data.append(weather.current.kind)


async def weather_forecast(town: str):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(town)
        print(weather)

        for forecast in weather.forecasts:
            forecast_weather.append(forecast)
    print(forecast_weather[0])
    return forecast_weather


def get_weather_forecast(town: str) -> list:
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(weather_forecast(town=town))
    return forecast_weather


def get_data(town: str) -> list:
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(getweather(town))
    return data


if __name__ == "__main__":
    test = get_weather_forecast("L")
    print(test[0].date)
