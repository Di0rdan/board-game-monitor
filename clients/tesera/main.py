from clients.tesera import api
import pprint


def main():
    client = api.DefaultTeseraClient()
    pprint.pprint(client.find_game_by_name("Иниш").to_json())


if __name__ == "__main__":
    main()
