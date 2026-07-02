# ♃ ☿ 𓂀  SQLITE MANAGER LAYER 𓂀  ☿ ♃


from pathlib import Path

import aiosqlite


class SQLiteManager:

    # SQLite database manager.

    def __init__(
        self,
        database_path: Path,
    ) -> None:

        self.database_path = database_path
        self.connection: aiosqlite.Connection | None = None

    async def connect(self) -> None:

        # Connect to database.

        self.connection = await aiosqlite.connect(
            self.database_path,
        )

        self.connection.row_factory = aiosqlite.Row

    async def close(self) -> None:

        # Close database connection.

        if self.connection is not None:
            await self.connection.close()

    async def execute(
        self,
        query: str,
        parameters: tuple = (),
    ) -> None:

        # Execute SQL query.

        if self.connection is None:
            raise RuntimeError(
                "Database is not connected."
            )

        await self.connection.execute(
            query,
            parameters,
        )

        await self.connection.commit()

    async def fetch_one(
        self,
        query: str,
        parameters: tuple = (),
    ) -> dict | None:

        # Fetch one record.

        if self.connection is None:
            raise RuntimeError(
                "Database is not connected."
            )

        cursor = await self.connection.execute(
            query,
            parameters,
        )

        row = await cursor.fetchone()

        if row is None:
            return None

        return dict(row)

    async def fetch_all(
        self,
        query: str,
        parameters: tuple = (),
    ) -> list[dict]:

        # Fetch all records.

        if self.connection is None:
            raise RuntimeError(
                "Database is not connected."
            )

        cursor = await self.connection.execute(
            query,
            parameters,
        )

        rows = await cursor.fetchall()

        return [
            dict(row)
            for row in rows
        ]
