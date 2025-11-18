from handlers.news_handlers import show_news, render_news
from handlers.canteen_handlers import show_canteen, render_canteen
from handlers.admin_handlers import admin_entry, admin_process


async def callback(update, context):
    q = update.callback_query
    data = q.data

    # =====================
    # ❌ Пустая неактивная кнопка
    # =====================
    if data == "noop":
        return await q.answer()  # ничего не делаем

    # =====================
    # ⚙ Вход в админ-панель
    # =====================
    if data == "admin":
        return await admin_entry(q, context)

    # =====================
    # 📰 Новости — открыть
    # =====================
    if data == "news_show":
        return await show_news(q, context)

    # Листание новостей
    if data == "news_prev":
        context.user_data["news_page"] = max(0, context.user_data.get("news_page", 0) - 1)
        return await render_news(q, context)

    if data == "news_next":
        context.user_data["news_page"] = context.user_data.get("news_page", 0) + 1
        return await render_news(q, context)

    # =====================
    # 🍽 Столовая — открыть
    # =====================
    if data == "canteen_show":
        return await show_canteen(q, context)

    # Листание меню столовой
    if data == "canteen_prev":
        context.user_data["canteen_page"] = max(0, context.user_data.get("canteen_page", 0) - 1)
        return await render_canteen(q, context)

    if data == "canteen_next":
        context.user_data["canteen_page"] = context.user_data.get("canteen_page", 0) + 1
        return await render_canteen(q, context)

    # =====================
    # ⚙ Остальные действия администратора
    # =====================
    if data.startswith("admin_") or data == "back_main":
        return await admin_process(q, context)

    # если что-то необработанное:
    return await q.answer("Неизвестная команда")