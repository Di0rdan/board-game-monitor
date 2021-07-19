import configparser
import logging

import bot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logging.getLogger("clients.tesera.api").setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)
config = configparser.ConfigParser()
config.read("config.ini")


def main():
    telegram_bot = bot.TelegramBot(config["telegram"]["AccessToken"])
    telegram_bot.register_handlers()

    telegram_bot.start()


if __name__ == "__main__":
    main()
