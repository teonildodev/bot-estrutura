from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = '7978229973:AAEgzOUzu-DO-Iv0wTJYSnI781tEQyFlkeM'

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower().replace(" ", "")
    caminho_imagem = f"estruturas/{texto}.jpg"
    
    if os.path.exists(caminho_imagem):
        await update.message.reply_photo(photo=open(caminho_imagem, 'rb'))
    else:
        await update.message.reply_text("Estrutura não encontrada. Verifique o nome e tente novamente.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot rodando...")
app.run_polling()

