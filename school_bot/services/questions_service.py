import aiosqlite
from .database import DB

async def add_question(user_id, username, text):
    async with aiosqlite.connect(DB) as db:
        await db.execute("INSERT INTO questions (user_id, username, text) VALUES (?, ?, ?)",
                         (user_id, username, text))
        await db.commit()