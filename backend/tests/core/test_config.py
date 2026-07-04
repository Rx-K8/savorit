from app.core.config import Settings, parse_cors


def test_settings_default_values() -> None:
    settings = Settings.model_validate({})

    assert settings.PROJECT_NAME == "savorit"
    assert settings.API_V1_STR == "/api/v1"
    assert settings.ENVIRONMENT == "local"
    assert settings.FRONTEND_HOST == "http://localhost:5173"
    assert settings.BACKEND_CORS_ORIGINS == []
    assert settings.all_cors_origins == ["http://localhost:5173"]


def test_parse_comma_separated_cors_origins() -> None:
    origins = parse_cors("http://localhost:3000, https://example.com")

    assert origins == [
        "http://localhost:3000",
        "https://example.com",
    ]


def test_settings_all_cors_origins_includes_frontend_host() -> None:
    settings = Settings.model_validate(
        {
            "BACKEND_CORS_ORIGINS": [
                "http://localhost:3000",
                "https://example.com",
            ]
        }
    )

    assert settings.all_cors_origins == [
        "http://localhost:3000",
        "https://example.com",
        "http://localhost:5173",
    ]
