from services.news_service import get_news
from views.pagination import pager
from telegram import InputMediaPhoto
from views.templates import NEWS_EMPTY

async def show_news(q, context):
    context.user_data["news_page"] = 0
    return await render_news(q, context)


async def render_news(q, context):
    news = await get_news()

    if not news:
        return await q.edit_message_text(NEWS_EMPTY)

    page = context.user_data["news_page"]
    id_, text, photo = news[page]

    await q.edit_message_media(
        InputMediaPhoto(photo, caption=text),
        reply_markup=pager(page, len(news), "news")
    )