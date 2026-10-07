import os


def get_api_key() -> str:
    return os.getenv("MEDILINK_API_KEY", "local-demo-key")


def get_request_timeout() -> int:
    raw = os.getenv("REQUEST_TIMEOUT", "5")
    try:
        value = int(raw)
    except (TypeError, ValueError) as exc:
        raise ValueError("REQUEST_TIMEOUT must be a valid integer greater than zero") from exc
    if value <= 0:
        raise ValueError("REQUEST_TIMEOUT must be greater than zero")
    return value

