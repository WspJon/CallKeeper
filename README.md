# 24/7 Discord AFK Voice Bot

A lightweight Python Discord bot using `discord.py` that stays in a Voice Channel 24/7 to keep the call timer active.

## Features
- **Automatic Reconnection Loop**: Checks voice connection state every 10 seconds and automatically reconnects if kicked or disconnected.
- **Bandwidth Saver**: Deafens and mutes itself upon joining.
- **Self-Healing**: Handles being moved to wrong channels or dropped connection gracefully.

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- A Discord Bot Token ([Discord Developer Portal](https://discord.com/developers/applications))

### 2. Installation
Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd discord_afk_bot
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configuration
Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

Edit `.env`:
```env
DISCORD_TOKEN=your_bot_token_here
VOICE_CHANNEL_ID=your_voice_channel_id_here
```

### 4. Running the Bot
```bash
python bot.py
```

## License
MIT
