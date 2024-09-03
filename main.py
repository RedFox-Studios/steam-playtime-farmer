import json
from farmer.steam_login import SteamLogin
from farmer.game_manager import GameManager
from farmer.utils import is_user_playing

def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

def main():
    config = load_config()
    steam_login = SteamLogin(config)
    steam_login.login()

    session = steam_login.get_session()
    game_manager = GameManager(session, config["GAMES"])

    while True:
        if is_user_playing(session):
            print("User is currently playing a game, pausing farming.")
        else:
            print("Resuming farming.")
            game_manager.start_farming()
        time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    main()