from telegram import Update , ext


Token = '7416684076:AAFqwWTpWKtPWsrOvv-SYODKthb1QE5xU70'
bot_username = '@today_pivot_pointbot'

async def help_command(update= Update, context= ext.ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(""" This are the commaands that are available
/start - starts the bot
/help - this commend show you the commends
/today_pivot_point - gives pairs that pivot point might work on for today
""")

async def handle_message(update= Update, context= ext.ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User({update.message.chat.id}) in {message_type}:'{text}'")


async def error(update= Update, context= ext.ContextTypes.DEFAULT_TYPE):
    print(f"{update} caused error {context.error}")



if __name__ == '__main__':
    app = ext.Application.builder().token(Token).build()

    app.add_handler(ext.CommandHandler('help', help_command))
    app.add_handler(ext.MessageHandler(ext.filters.ALL, handle_message))
    
    app.add_error_handler(error)    

    print("polling...")
    app.run_polling(poll_interval=3)

#from telethon import TelegramClient
#
## Replace these with your own values
#api_id = 'YOUR_API_ID'
#api_hash = 'YOUR_API_HASH'
#phone_number = '+98 904 685 0226'
#
## Create the client and connect
#client = TelegramClient('session_name', api_id, api_hash)
#
#async def main():
#    # Log in if required
#    if not await client.is_user_authorized():
#        await client.send_code_request(phone_number)
#        code = input('Enter the code: ')
#        await client.sign_in(phone_number, code)
#
#    # Get messages from a specific chat
#    chat = 'chat_username_or_id'
#    messages = await client.get_messages(chat, limit=10)
#
#    for message in messages:
#        print(message.sender_id, message.text)
#
#with client:
#    client.loop.run_until_complete(main())
#