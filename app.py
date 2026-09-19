import os

from dotenv import load_dotenv
from flask import Flask

from routes.weather_routes import weather_bp


def create_app(test_config=None):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "development-only-secret"),
        WEATHER_API_KEY=os.getenv("WEATHER_API_KEY", ""),
        GROQ_API_KEY=os.getenv("GROQ_API_KEY", ""),
    )

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(weather_bp)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
