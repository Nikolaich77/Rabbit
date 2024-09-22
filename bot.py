import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Увімкнення логування
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# встановлення вищого рівня логування для httpx, щоб уникнути логування всіх GET і POST запитів
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Визначення кількох обробників команд. Зазвичай вони приймають два аргументи: update і context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Надсилає повідомлення, коли виконується команда /start."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привіт {user.mention_html()}! Я підослідний кролик врятуйте мене будь ласка.",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Надсилає повідомлення, коли виконується команда /help."""
    await update.message.reply_text("Допоможіть!")

# Функція обробки текстових повідомлень (echo)
async def echo_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

# Функція обробки GIF (echo)
async def echo_gif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_animation(update.message.animation.file_id)

# Функція обробки наліпок (echo)
async def echo_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_sticker(update.message.sticker.file_id)

def main() -> None:
    """Запуск бота."""
    # Створення додатку та передача токену вашого бота.
    application = Application.builder().token("7818534299:AAFcQcJN4xMaOKq6kSJSIQjAQDN7AMK8F2o").build()

    # на різні команди - відповідь у Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Реєстрація обробника текстових повідомлень
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_text))
    
    # Реєстрація обробника GIF
    application.add_handler(MessageHandler(filters.ANIMATION, echo_gif))
    
    # Реєстрація обробника наліпок
    application.add_handler(MessageHandler(filters.Sticker.ALL, echo_sticker))

    # Запуск бота до тих пір, поки користувач не натисне Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()