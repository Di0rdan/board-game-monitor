import logging

import bot

TOKEN = "1916132812:AAGLN-5c4Io_uXQOaRyy62SobDBD9zDC0zk"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    telegram_bot = bot.TelegramBot(TOKEN)
    telegram_bot.register_handlers()

    telegram_bot.start()


if __name__ == "__main__":
    main()
