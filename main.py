from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import asyncio

import infoDeMarket

token = ""
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
    asyncio.create_task(give_em_info(context.application))

async def stopinfo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Someone stopped recieving information.")
    chat_id = update.effective_chat.id
    user_subscriptions[chat_id] = False
    await update.message.reply_text("You're no longer recieving information.")
    print(user_subscriptions.items())


#ASIL OLAY
async def give_em_info(app: Application) -> None:
    print("Sending info to someone")
    fag = True
    while True:
        infoA = infoDeMarket.CoinMarketCapInfo()
        for chatid, subscribed in user_subscriptions.items():
            if subscribed:
                try:
                    if fag:
                        await app.bot.send_message(chat_id=chatid, text=infoA)                   
                except:
                    print(f"Failed to send message to {chatid}:")
        await asyncio.sleep(5)
        if infoA != infoDeMarket.CoinMarketCapInfo():
            fag = True
            print(infoDeMarket.CoinMarketCapInfo())
        else:
            fag = False
            print("Prices hasnt changed")




if __name__ == "__main__":
    app = Application.builder().token(token).build()


    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("infome", infome_command))
    app.add_handler(CommandHandler("stopinfo", stopinfo_command))


    app.run_polling()
