# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations


from pathlib import Path
import sqlite3


class Database:
    """
    SQLite database connection manager.
    """


    def __init__(
        self,
        path: str,
    ) -> None:

        self.path = Path(path)

        self.connection: sqlite3.Connection | None = None



    def connect(
        self,
    ) -> sqlite3.Connection:

        if self.connection is None:

            self.path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            self.connection = sqlite3.connect(
                self.path,
            )

            self.connection.row_factory = sqlite3.Row


        return self.connection



    def close(
        self,
    ) -> None:

        if self.connection:

            self.connection.close()

            self.connection = None



    def execute(
        self,
        query: str,
        parameters: tuple = (),
    ) -> sqlite3.Cursor:

        connection = self.connect()

        cursor = connection.execute(
            query,
            parameters,
        )

        connection.commit()

        return cursor



    def executescript(
        self,
        script: str,
    ) -> None:

        connection = self.connect()

        connection.executescript(
            script,
        )

        connection.commit()