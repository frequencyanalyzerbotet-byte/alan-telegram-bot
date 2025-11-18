import aiosqlite
from .database import DB

async def add_canteen(day, text, photo):
    async with aiosqlite.connect(DB) as db:
        await db.execute("INSERT INTO canteen(day, text, photo) VALUES (?, ?, ?)",
                         (day, text, photo))
        await db.commit()

async def get_canteen():
    async with aiosqlite.connect(DB) as db:
        cur = await db.execute("SELECT id, day, text, photo FROM canteen ORDER BY id")
        return await cur.fetchall()