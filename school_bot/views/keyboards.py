from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📰 Новости", callback_data="news_show")],
        [InlineKeyboardButton("🍽 Меню столовой", callback_data="canteen_show")],
        [InlineKeyboardButton("⚙️ Админ-панель", callback_data="admin")]
    ])


def admin_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Новость", callback_data="admin_add_news")],
        [InlineKeyboardButton("➕ Меню столовой", callback_data="admin_add_canteen")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="back_main")],
    ])
