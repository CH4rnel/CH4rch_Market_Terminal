from backend.core.config import load_config


def main():
    cfg = load_config()

    print("APP NAME:", cfg.app.name)
    print("ENV:", cfg.app.environment)
    print("DB:", cfg.database.path)
    print("DEXSCREENER ENABLED:", cfg.providers["dexscreener"].enabled)


if __name__ == "__main__":
    main()
