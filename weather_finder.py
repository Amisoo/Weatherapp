from typing import List, Any

import python_weather

import asyncio
import os

kind_dict = {
    "SUNNY": 1,
    "PARTLY_CLOUDY": 2,
    "CLOUDY": 3,
    "VERY_CLOUDY": 4,
    "FOG": 5,
    "LIGHT_SHOWERS": 6,
    "LIGHT_SLEET_SHOWERS": 7,
    "LIGHT_SLEET": 8,
    "THUNDERY_SHOWERS": 9,
    "LIGHT_SNOW": 10,
    "HEAVY_SNOW": 11,
    "LIGHT_RAIN": 12,
    "HEAVY_SHOWERS": 13,
    "HEAVY_RAIN": 14,
    "LIGHT_SNOW_SHOWERS": 15,
    "HEAVY_SNOW_SHOWERS": 16,
    "THUNDERY_HEAVY_RAIN": 17,
    "THUNDERY_SNOW_SHOWERS": 18,
}

data: list[Any] = []


async def getweather(town: str):
    kind_list = []

    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(town)

        data.append(weather.current.temperature)
        data.append(weather.current.kind)

        """
        for forecast in weather.forecasts:
            kind_in_list = [forecast]

            for hourly in forecast.hourly:
                kind_in_list.append(str(hourly.kind).upper())
            kind_list.append(kind_in_list)
        """


def get_data(town: str) -> list:
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(getweather(town))
    return data
