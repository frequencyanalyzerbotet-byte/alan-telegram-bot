import asyncio
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)
from config import TOKEN
from services.database import init_db
from handlers.user_handlers import start
from handlers.callback_router import callback
from handlers.admin_handlers import admin_message

# ======================
# Создаём явный цикл событий
# ======================
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# ======================
# Инициализация базы данных
# ======================
loop.run_until_complete(init_db())

# ======================
# Создаём приложение
# ======================
app = Application.builder().token(TOKEN).build()

# ======================
# Команды и хэндлеры
# ======================
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(callback))
app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, admin_message))

# ======================
# Запуск бота
# ======================
print("🤖 Бот запущен!")
app.run_polling()