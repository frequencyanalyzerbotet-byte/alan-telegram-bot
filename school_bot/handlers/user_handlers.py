from views.keyboards import main_menu
from views.templates import MAIN_MENU

async def start(update, context):
    await update.message.reply_text(MAIN_MENU, reply_markup=main_menu())