from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    message = 'Olá ' + str(update.message.from_user.username) + '. Tudo bem?'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token = '1179070933:AAGW5gDZ-1FCECKV1M0q4DLxLR8hoLWNrUQ'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.start_polling()
    print(str(updater))
    updater.idle()

if __name__ == "__main__":
    main()