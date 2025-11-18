import os

# =========================
# 🔑 TOKEN TELEGRAM
# =========================
TOKEN = "8517916519:AAFZGk2KcbJuu9xyH9jJtJLrgsrfnv8vd5g"

# =========================
# 👤 ADMIN IDS
# Сюда добавляем Telegram ID админов
# =========================
ADMIN_IDS = [
    7589163106,  # пример ID директора
    987654321,  # пример ID учителя
]

# =========================
# 🗄 DATABASE
# SQLite файл
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "school_bot.db")

# =========================
# 📂 STATIC (картинки)
# Папка со школьными картинками
# =========================
STATIC_DIR = os.path.join(BASE_DIR, "static")

# =========================
# 🕹 НАСТРОЙКИ ПАГИНАЦИИ
# =========================
ITEMS_PER_PAGE = 1  # для новостей и меню столовой