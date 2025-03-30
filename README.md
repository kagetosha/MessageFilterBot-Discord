# Discord Bot for Censorship

This is a simple Discord bot that deletes messages containing forbidden words and notifies the user of the reason.

## Features
- The bot checks incoming messages for forbidden words.
- If any forbidden words are found, the message is deleted.
- The bot notifies the user of the deletion and the reason in the channel.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/kagetosha/MessageFilterBot-Discord.git
    ```

2. Install the required dependencies:
    ```bash
    pip install disnake
    ```

3. Create a new bot on the [Discord Developer Portal](https://discord.com/developers/applications), get the token, and replace the `TOKEN` variable in the code (inside `main.py`) with your bot token.

4. Run the bot:
    ```bash
    python main.py
    ```

## Usage

Once the bot is running, it will automatically start monitoring messages for forbidden words. If a message contains any of the forbidden words, it will be deleted, and the user will be notified.

## Contributing

Feel free to fork the repository and submit pull requests if you have improvements or fixes.
