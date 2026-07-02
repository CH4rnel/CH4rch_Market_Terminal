import asyncio
from pathlib import Path

from ch4rch_market.storage.sqlite_manager import SQLiteManager


async def main() -> None:

    database = SQLiteManager(
        Path("test.db"),
    )

    await database.connect()

    await database.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
        """
    )

    await database.execute(
        "INSERT INTO users (name) VALUES (?)",
        ("CH4rch",),
    )

    user = await database.fetch_one(
        "SELECT * FROM users"
    )

    print(user)

    await database.close()


asyncio.run(main())
