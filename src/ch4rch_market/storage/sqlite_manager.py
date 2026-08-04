# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from __future__ import annotations


from ch4rch_market.core.logger import logger
from ch4rch_market.storage.database import Database



class SQLiteManager:
    """
    SQLite lifecycle manager.
    """



    def __init__(
        self,
        database: Database,
    ) -> None:

        self.database = database



    async def start(
        self,
    ) -> None:

        self.database.connect()


        self.database.executescript(
            """
            CREATE TABLE IF NOT EXISTS pairs (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                symbol TEXT UNIQUE NOT NULL,

                exchange TEXT NOT NULL

            );


            CREATE TABLE IF NOT EXISTS candles (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                symbol TEXT NOT NULL,

                timeframe TEXT NOT NULL,

                open REAL,

                high REAL,

                low REAL,

                close REAL,

                volume REAL,

                timestamp INTEGER

            );


            CREATE TABLE IF NOT EXISTS trades (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                symbol TEXT NOT NULL,

                price REAL,

                quantity REAL,

                timestamp INTEGER

            );

            """
        )


        logger.info(
            "sqlite_started",
            path=str(self.database.path),
        )



    async def stop(
        self,
    ) -> None:


        self.database.close()


        logger.info(
            "sqlite_stopped",
        )