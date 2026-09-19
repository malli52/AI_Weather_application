# AI Weather App

A Flask weather dashboard powered by OpenWeatherMap, with optional concise weather advice from Groq.

## Setup

1. Create and activate a virtual environment.
2. Run `pip install -r requirements.txt`.
3. Copy the values in `.env` with your API keys (do not commit this file).
4. Start the app with `flask --app app run --debug`.

Visit `http://127.0.0.1:5000`, search for a city, and run `pytest` for the starter test suite.

## Routes

- `GET /` — dashboard
- `GET /api/weather?city=Delhi` — current weather JSON
