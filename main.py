from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import asyncio


import infoDeMarket


token = "7063934191:AAGR1HY63Dp-_YHbeJF2sEtwtQ4RuLbq0dE"
bot_username = "@StockMarketInfoGrabberBot"



#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("To get info from different stock markets every minute:\n/infome\n For me to stop:\n/stopinfo")



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("To get info from different stock markets every minute:\n/infome\n For me to stop:\n/stopinfo")

user_subscriptions = {}


async def infome_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_subscriptions[chat_id] = True
    await update.message.reply_text("You will start receiving messages. It'll automatically stop in 30 minutes.")
    print(user_subscriptions.items())
    await give_em_info(app)

async def stopinfo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_subscriptions[chat_id] = False
    await update.message.reply_text("You're no longer recieving information.")
    print(user_subscriptions.items())


#ASIL OLAY
async def give_em_info(app: Application) -> None:
    print("Sending info to someone")
    while True:
        for chatid, subscribed in user_subscriptions.items():
            if subscribed:
                try:
                    await app.bot.send_message(chat_id=chatid, text=infoDeMarket.GatherAll())
                except:
                    print(f"Failed to send message to {chatid}:")
        await asyncio.sleep(10)





if __name__ == "__main__":
    app = Application.builder().token(token).build()


    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("infome", infome_command))
    app.add_handler(CommandHandler("stopinfo", stopinfo_command))


    app.run_polling()