from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def pager(current, total, prefix):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("◀️", callback_data=f"{prefix}_prev" if current > 0 else "noop"),
            InlineKeyboardButton(f"{current+1}/{total}", callback_data="noop"),
            InlineKeyboardButton("▶️", callback_data=f"{prefix}_next" if current < total-1 else "noop"),
        ]
    ])