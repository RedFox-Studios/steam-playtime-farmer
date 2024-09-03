# Steam Playtime Farmer

Steam Playtime Farmer is a Python application that simulates playing multiple games on Steam to increase your playtime hours effortlessly. The program runs in the background, launching specified games while you are away, and pauses automatically if you start playing a game manually.

## Features

- Emulate playing up to 32 games simultaneously.
- Automatically pauses when the user starts playing any Steam game.
- Automatically resumes when the user finishes playing.
- Keeps the user's Steam profile in invisible mode to hide activity.
- Configuration through a `config.json` file.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/steam-playtime-farmer.git
    cd steam-playtime-farmer
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure your account:**

    - Edit the `config.json` file with your Steam credentials and the game IDs you want to farm.

5. **Run the application:**

    ```bash
    python main.py
    ```

## Configuration

- `ACCOUNT_NAME`: Your Steam account name.
- `PASSWORD`: Your Steam account password.
- `SHARED_SECRET`: Your 2FA shared secret (optional, but required if 2FA is enabled).
- `GAMES`: A list of game IDs to farm.

## License

This project is licensed under the MIT License.
