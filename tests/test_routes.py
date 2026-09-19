from app import create_app


def test_index_loads():
    app = create_app({"TESTING": True})
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"AI Weather" in response.data


def test_weather_endpoint_requires_configured_key():
    app = create_app({"TESTING": True, "WEATHER_API_KEY": ""})
    response = app.test_client().get("/api/weather?city=Delhi")
    assert response.status_code == 400
