import pytest

from services.weather_service import WeatherService, WeatherServiceError


def test_empty_city_is_rejected():
    with pytest.raises(WeatherServiceError, match="city"):
        WeatherService("key").get_weather("")


def test_missing_key_is_rejected():
    with pytest.raises(WeatherServiceError, match="API_KEY"):
        WeatherService("").get_weather("Delhi")
