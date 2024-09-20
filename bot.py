import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Дозволяємо вкладені цикли
nest_asyncio.apply()

# Функція обробки команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привіт! Я підослідний кролик врятуйте мене будь ласка.')

async def main():
    # Введіть свій токен тут
    application = ApplicationBuilder().token("7818534299:AAFcQcJN4xMaOKq6kSJSIQjAQDN7AMK8F2o").build()

    # Реєстрація обробника команд
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    await application.run_polling()

if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
