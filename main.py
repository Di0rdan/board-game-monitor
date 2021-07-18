import logging

import bot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    telegram_bot = bot.TelegramBot()
    telegram_bot.register_handlers()

    telegram_bot.start()


if __name__ == "__main__":
    main()
