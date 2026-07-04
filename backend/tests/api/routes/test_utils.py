from fastapi.testclient import TestClient

from app.main import app


def test_app_uses_configured_metadata() -> None:
    assert app.title == "savorit"
    assert app.openapi_url == "/api/v1/openapi.json"


def test_health_check() -> None:
    client = TestClient(app)

    response = client.get("/api/v1/utils/health-check/")

    assert response.status_code == 200
    assert response.json() is True
