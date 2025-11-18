from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_IDS
from views.keyboards import admin_menu, main_menu
from services.news_service import add_news
from services.canteen_service import add_canteen


# =======================================================
# 🔐 Проверка прав администратора
# =======================================================

def is_admin(uid: int) -> bool:
    return uid in ADMIN_IDS


# =======================================================
# ⚙️ Вход в админ-панель
# =======================================================

async def admin_entry(q, context):
    uid = q.from_user.id

    if not is_admin(uid):
        return await q.answer("Нет доступа ❌", show_alert=True)

    await q.edit_message_text("⚙️ Админ-панель:", reply_markup=admin_menu())


# =======================================================
# 📌 Пошаговые режимы:
# news_text → news_photo  
# canteen_day → canteen_text → canteen_photo
# =======================================================


# =======================================================
# 📝 Обработка кнопок из админ-панели
# =======================================================

async def admin_process(q, context):
    data = q.data
    uid = q.from_user.id

    if not is_admin(uid):
        return await q.answer("Нет доступа ❌", show_alert=True)

    # -------- Добавить новость --------
    if data == "admin_add_news":
        context.user_data["mode"] = "news_text"
        return await q.edit_message_text("📰 Введите текст новости:")

    # -------- Добавить меню столовой --------
    if data == "admin_add_canteen":
        context.user_data["mode"] = "canteen_day"
        return await q.edit_message_text("🍽 Введите день недели:")

    # кнопка назад
    if data == "back_main":
        context.user_data["mode"] = None
        return await q.edit_message_text("Главное меню:", reply_markup=main_menu())


# =======================================================
# 📨 Обработка текстов и фотографий (ввод администратора)
# =======================================================

async def admin_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = context.user_data.get("mode")

    # -----------------------------------------------
    # 1️⃣ ДОБАВЛЕНИЕ НОВОСТИ
    # -----------------------------------------------

    # Шаг 1: ввод текста новости
    if mode == "news_text":
        context.user_data["news_text"] = update.message.text
        context.user_data["mode"] = "news_photo"
        return await update.message.reply_text(
            "🖼 Теперь отправьте фото для новости."
        )

    # Шаг 2: получение фото
    if mode == "news_photo":
        if not update.message.photo:
            return await update.message.reply_text("Отправьте фото!")

        photo_id = update.message.photo[-1].file_id
        text = context.user_data["news_text"]

        await add_news(text=text, photo=photo_id)

        context.user_data["mode"] = None
        return await update.message.reply_text(
            "✅ Новость успешно добавлена!",
            reply_markup=main_menu()
        )

    # -----------------------------------------------
    # 2️⃣ ДОБАВЛЕНИЕ МЕНЮ СТОЛОВОЙ
    # -----------------------------------------------

    # Шаг 1: ввод дня недели
    if mode == "canteen_day":
        context.user_data["day"] = update.message.text
        context.user_data["mode"] = "canteen_text"
        return await update.message.reply_text(
            "Введите описание меню:"
        )

    # Шаг 2: ввод описания меню
    if mode == "canteen_text":
        context.user_data["canteen_text"] = update.message.text
        context.user_data["mode"] = "canteen_photo"
        return await update.message.reply_text(
            "🖼 Теперь отправьте фото меню:"
        )

    # Шаг 3: получение фото меню
    if mode == "canteen_photo":
        if not update.message.photo:
            return await update.message.reply_text("Отправьте фото!")

        day = context.user_data["day"]
        text = context.user_data["canteen_text"]
        photo = update.message.photo[-1].file_id

        await add_canteen(day=day, text=text, photo=photo)

        context.user_data["mode"] = None
        return await update.message.reply_text(
            "✅ Меню столовой добавлено!",
            reply_markup=main_menu()
        )

    # Ничего не делаем, если режим пуст
    return