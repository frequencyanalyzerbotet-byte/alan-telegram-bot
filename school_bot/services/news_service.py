from .database import DB
import aiosqlite

async def add_news(text, photo):
    async with aiosqlite.connect(DB) as db:
        await db.execute("INSERT INTO news (text, photo) VALUES (?, ?)", (text, photo))
        await db.commit()

async def get_news():
    async with aiosqlite.connect(DB) as db:
        cur = await db.execute("SELECT id, text, photo FROM news ORDER BY id DESC")
        return await cur.fetchall()
