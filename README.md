# 24/7 Discord Voice Channel AFK Keeper

A lightweight tool using `discord.py` that stays in a Voice Channel 24/7 to keep call timers running indefinitely.

## Features
- **Automatic Reconnection Loop**: Checks voice connection state every 10 seconds and automatically reconnects if dropped or disconnected.
- **Zero Bandwidth**: Deafens and mutes upon joining to conserve bandwidth.
- **Self-Healing**: Handles network interruptions and voice server resets gracefully.

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- Token & Voice Channel ID

### 2. Installation
Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd discord_afk_bot
python -m venv venv

# On Windows:
.\venv\Scripts\activate
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
DISCORD_TOKEN=your_token_here
VOICE_CHANNEL_ID=your_voice_channel_id_here
```

### 4. Running the Script
```bash
python bot.py
```

## License
MIT
