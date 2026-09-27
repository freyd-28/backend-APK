import os
from src import create_app


def env_bool(value, default=False):
    if value is None:
        return default
    return str(value).strip().lower() in {"true", "1", "yes", "on", "t"}


app = create_app(os.getenv("FLASK_CONFIG", "development"))


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug_mode = env_bool(os.getenv("DEBUG", "True"), True)

    print()
    print("=" * 50)
    print(" BilleterAPP API - MINI APK")
    print("=" * 50)
    print(f" Servidor: http://localhost:{port}")
    print(f" API:      http://localhost:{port}/api/v1")
    print(f" Debug:    {debug_mode}")
    print("=" * 50)
    print()

    app.run(host="0.0.0.0", port=port, debug=debug_mode)
