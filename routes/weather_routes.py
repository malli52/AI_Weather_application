from flask import Blueprint, current_app, jsonify, render_template, request

from services.groq_service import GroqService
from services.weather_service import WeatherService, WeatherServiceError

weather_bp = Blueprint("weather", __name__)


@weather_bp.get("/")
def index():
    return render_template("index.html")


@weather_bp.get("/api/weather")
def weather():
    city = request.args.get("city", "")
    service = WeatherService(current_app.config["WEATHER_API_KEY"])
    try:
        forecast = service.get_weather(city)
    except WeatherServiceError as error:
        return jsonify({"error": str(error)}), 400

    forecast["advice"] = GroqService(current_app.config["GROQ_API_KEY"]).get_advice(forecast)
    return jsonify(forecast)
