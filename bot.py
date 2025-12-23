from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

#TOKEN = "7947726214:AAFgHoQ-LrOYymVOqppbXkU-WP8pvN0fbtg"

# Owner username
OWNER = "@GXBOSS2"

# USDT TRC20 Address
USDT_ADDRESS = "TDNF1LXdQCyCXvEhYpS8ATkGNPHAaui7tE"

# Start / welcome message
def start(update: Update, context: CallbackContext):
    welcome_text = f"""
𝑯𝒆𝒍𝒍𝒐 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 To The 
verifying Master

Here You Get It one Package

Any Bin Added On Your Ads By Our Bot

Price List ↓

15 day - 30$
30 day - 50$

If You Want To Buy → Click [ BUY ACCESS ] ♻️
"""
    keyboard = [
        [InlineKeyboardButton("BUY ACCESS", callback_data='buy_access')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Button clicks
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    if query.data == 'buy_access':
        keyboard = [
            [InlineKeyboardButton("15 Days - 30$", callback_data='15days')],
            [InlineKeyboardButton("31 Days - 50$", callback_data='31days')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            text=f"Choose your plan:\n\nSend payment to USDT TRC20:\n{USDT_ADDRESS}\n\nAfter payment, send screenshot here.\nOwner: {OWNER}",
            reply_markup=reply_markup
        )
    elif query.data in ['15days', '31days']:
        plan = "15 Days - 30$" if query.data == '15days' else "31 Days - 50$"
        query.edit_message_text(
            text=f"You chose: {plan}\n\nSend payment to USDT TRC20:\n{USDT_ADDRESS}\nAfter payment, send screenshot here.\nOwner: {OWNER}"
        )

# Handle messages/screenshots
def handle_messages(update: Update, context: CallbackContext):
    update.message.reply_text(f"Thanks! Your screenshot has been received.\nOwner: {OWNER}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text | Filters.photo, handle_messages))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
