import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower().replace(" ", "")
    base = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(base, "estruturas", f"{texto}.jpg")
    if os.path.exists(caminho):
        await update.message.reply_photo(photo=open(caminho, 'rb'))
    else:
        await update.message.reply_text("Estrutura não encontrada.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    print("Bot rodando...")
    app.run_polling()
