import logging
import asyncio
import aiohttp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

# Токен вашого бота та токен іншого бота
BOT_TOKEN = '7304454295:AAGTCxIKt8Trad2wsTRoxyjKcK12eBXbltk'
TARGET_BOT_TOKEN = '7818534299:AAFcQcJN4xMaOKq6kSJSIQjAQDN7AMK8F2o'

# URL API іншого бота
TARGET_BOT_URL = f"https://api.telegram.org/bot{TARGET_BOT_TOKEN}/sendMessage"

# Логування для зручності
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Список chat_id, до яких будемо надсилати запити на іншого бота
target_chat_ids = [123456789, 987654321, 1122334455]  # Замінити на реальні ID

async def send_request_to_another_bot(session: aiohttp.ClientSession, chat_id: int, message: str):
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    try:
        async with session.post(TARGET_BOT_URL, json=payload) as response:
            if response.status == 200:
                logger.info(f"Message sent to chat_id {chat_id}")
            else:
                logger.error(f"Failed to send message to chat_id {chat_id}: {response.status}")
    except Exception as e:
        logger.error(f"Error sending message to chat_id {chat_id}: {e}")

async def mass_send_to_another_bot(message: str):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for chat_id in target_chat_ids:
            tasks.append(send_request_to_another_bot(session, chat_id, message))
        await asyncio.gather(*tasks)

async def start(update: Update, context):
    # Стартова команда, яка запускає масову розсилку запитів на іншого бота
    message = "Mass request from another bot!"
    await update.message.reply_text("Starting mass request to another bot...")
    await mass_send_to_another_bot(message)
    await update.message.reply_text("Requests sent!")

if __name__ == '__main__':
    # Створюємо бота
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Додаємо хендлер для команди /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Запускаємо бота
    application.run_polling()