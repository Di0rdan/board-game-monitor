from clients.tesera import api
import pprint


def main():
    client = api.DefaultTeseraClient()
    pprint.pprint(client.search_games("Inis"))


if __name__ == "__main__":
    main()
