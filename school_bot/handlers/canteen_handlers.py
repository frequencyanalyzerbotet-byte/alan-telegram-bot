from services.canteen_service import get_canteen
from views.pagination import pager
from telegram import InputMediaPhoto
from views.templates import CANTEEN_EMPTY

async def show_canteen(q, context):
    context.user_data["canteen_page"] = 0
    return await render_canteen(q, context)


async def render_canteen(q, context):
    data = await get_canteen()

    if not data:
        return await q.edit_message_text(CANTEEN_EMPTY)

    page = context.user_data["canteen_page"]
    id_, day, text, photo = data[page]

    caption = f"🍽 *{day}*\n{text}"

    await q.edit_message_media(
        InputMediaPhoto(photo, caption=caption, parse_mode="Markdown"),
        reply_markup=pager(page, len(data), "canteen")
    )