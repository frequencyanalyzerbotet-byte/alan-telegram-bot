import aiosqlite

DB = "school.db"

async def init_db():
    async with aiosqlite.connect(DB) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                photo TEXT
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS canteen (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                day TEXT,
                text TEXT,
                photo TEXT
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                username TEXT,
                text TEXT
            )
        """)

        await db.commit()