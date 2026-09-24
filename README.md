# 🎙️ CallKeeper — 24/7 Discord Voice Channel AFK Keeper

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-v2.4.0-blueviolet.svg)](https://github.com/Rapptz/discord.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**CallKeeper** is a lightweight, self-healing Python bot designed to keep Discord voice call timers running indefinitely. It stays connected to a specified voice channel 24/7 and automatically reconnects if kicked, disconnected, or moved.

---

## ✨ Features

- 🔄 **Auto-Reconnect Loop**: Continuously checks voice connection status every 10 seconds and automatically reconnects if dropped.
- 🔇 **Zero-Bandwidth Idling**: Automatically mutes and deafens itself upon joining to minimize bandwidth and CPU usage.
- 🛠️ **Self-Healing**: Recovers gracefully from network interruptions, server restarts, or manual disconnects.
- 🔒 **Secure Configuration**: Uses environment variables (`.env`) to ensure bot tokens and sensitive IDs are never exposed.

---

## 🚀 Quick Start

### 1. Prerequisites
- [Python 3.8+](https://www.python.org/downloads/) installed on your machine.
- A **Discord Bot Token** and **Voice Channel ID**.

### 2. Installation

Clone the repository and set up a virtual environment:

```bash
# Clone this repository
git clone https://github.com/WspJon/CallKeeper.git
cd CallKeeper

# Create and activate a virtual environment
python -m venv venv

# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt
```

---

## ⚙️ Configuration

1. Copy the sample environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` in any text editor and fill in your credentials:
   ```env
   DISCORD_TOKEN=your_bot_token_here
   VOICE_CHANNEL_ID=your_voice_channel_id_here
   ```

> [!TIP]
> **How to get the Voice Channel ID:**
> Enable **Developer Mode** in Discord Settings -> Advanced. Right-click your desired voice channel and select **Copy Channel ID**.

---

## 🎮 Usage

Start the bot with:

```bash
python bot.py
```

You should see console logs indicating successful login and connection:

```text
Logged in as CallKeeper#1234 (ID: 987654321)
Bot is not in the channel. Attempting to connect to General...
Successfully connected to General
```

---

## ❓ FAQ

<details>
<summary><b>Why does the bot mute and deafen itself?</b></summary>
<br>
Deafening and muting reduces network overhead to near-zero, ensuring the bot can stay connected 24/7 without consuming unnecessary bandwidth or audio resources.
</details>

<details>
<summary><b>What happens if the bot is disconnected or kicked?</b></summary>
<br>
CallKeeper runs a background task loop every 10 seconds. If it detects that it was disconnected, moved, or dropped, it will automatically force its connection back into the target voice channel.
</details>

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
