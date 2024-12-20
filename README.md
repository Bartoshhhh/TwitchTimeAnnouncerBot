# TwitchTimeAnnouncerBot
A bot that announces the current time every 2 minutes in Twitch channel chats.


# TwitchTimeBot

A simple bot that announces the current time in a Twitch channel's chat every 2 minutes.

## Prerequisites

Before running the bot, make sure you have the following:

- A **Twitch account** (for both the bot and the channel to be used).
- Python 3.8 or higher installed.
- The following Python libraries installed: `twitchio`, `pytz`.

## Setup Instructions

### 1. Create a new Twitch account for your bot

- Visit [Twitch.tv](https://www.twitch.tv/) and create a new account.
- Choose a nickname for your bot (e.g., `TwitchTimeBot`), as this will be used in your bot's code.

### 2. Generate an OAuth token for your bot

- Go to [Twitch Token Generator](https://twitchtokengenerator.com/).
- Log in with your newly created Twitch bot account.
- Select the **"chat:read"** and **"chat:edit"** permissions (these allow the bot to read and send messages in the chat).
- Generate the token and **copy** it.

### 3. Edit the bot code

- Open the `bot.py` script you downloaded or created.
- Replace the placeholder `xxxx` with the following:
  - **Token**: Paste the OAuth token you copied from the Twitch Token Generator.
  - **Streamer Channel**: Replace the placeholder `xxxx` in `initial_channels=['xxxx']` with the **Twitch channel name** where you want the bot to announce the time (don't include `https://` or `.tv` — just the channel's nickname).

Example:

```python
token='your_oauth_token'  # Paste your token here
initial_channels=['streamer_username']  # Replace with the Twitch channel's name
