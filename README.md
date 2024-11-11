# DiscordCodeBot

DiscordCodeBot is a simple Discord bot that fetches and shares memes from the internet. It uses the `discord.py` library to interact with the Discord API and the `requests` library to fetch memes from the Meme API.

## Features

- Fetches random memes from the Meme API.
- Shares memes in a Discord channel.

## Setup

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/subba2048/DiscordCodeBot.git
    cd DiscordCodeBot
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

5. Create a [.env](http://_vscodecontentref_/1) file in the root directory and add your Discord bot token:
    ```env
    DISCORD_TOKEN=your_discord_token_here
    ```

6. Run the bot:
    ```sh
    python bot.py
    ```

## Usage

Once the bot is running, it will listen for commands in your Discord server and respond with memes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.