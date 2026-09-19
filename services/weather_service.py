"""OpenWeatherMap client."""

import requests


class WeatherServiceError(Exception):
    """Raised when weather data cannot be retrieved."""


class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key, session=requests):
        self.api_key = api_key
        self.session = session

    def get_weather(self, city):
        if not self.api_key:
            raise WeatherServiceError("WEATHER_API_KEY is not configured.")
        if not city or not city.strip():
            raise WeatherServiceError("Please provide a city name.")

        try:
            response = self.session.get(
                self.BASE_URL,
                params={"q": city.strip(), "appid": self.api_key, "units": "metric"},
                timeout=10,
            )
            response.raise_for_status()
        except requests.RequestException as error:
            if getattr(error.response, "status_code", None) == 404:
                raise WeatherServiceError("City not found. Try a more specific name.") from error
            raise WeatherServiceError("Weather service is unavailable. Please try again.") from error

        data = response.json()
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": round(data["main"]["temp"]),
            "feels_like": round(data["main"]["feels_like"]),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"].capitalize(),
            "icon": data["weather"][0]["icon"],
        }
