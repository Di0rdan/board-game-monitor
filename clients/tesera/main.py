from clients.tesera import api
import pprint


def main():
    client = api.DefaultTeseraClient()
    for game in client.generate_recommendation(["Иниш", "Киклады"]):
        pprint.pprint(game.to_json())


if __name__ == "__main__":
    main()
