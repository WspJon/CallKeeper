# 🎙️ CallKeeper — 24/7 Discord Voice Channel AFK Keeper

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-v2.4.0-blueviolet.svg)](https://github.com/Rapptz/discord.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**CallKeeper** is a lightweight, self-healing Python bot designed to stay connected in a Discord voice channel 24/7 to keep the call timer running indefinitely. It automatically reconnects if kicked, disconnected, or moved.

---

## 📋 Table of Contents
- [✨ Features](#-features)
- [📖 Step-by-Step Setup Guide](#-step-by-step-step-guide)
  - [Step 1: Get Discord Credentials](#step-1-get-discord-credentials)
  - [Step 2: Invite Bot to Server](#step-2-invite-bot-to-server)
  - [Step 3: Local Installation](#step-3-local-installation)
  - [Step 4: Configure Credentials](#step-4-configure-credentials)
  - [Step 5: Run the Bot](#step-5-run-the-bot)
- [🌐 24/7 Hosting Guide (Run Without PC On)](#-247-hosting-guide-run-without-pc-on)
  - [Option A: Free Hosting on Render.com](#option-a-free-hosting-on-rendercom-recommended)
  - [Option B: VPS / Linux Server (Ubuntu/Debian)](#option-b-vps--linux-server-ubuntudebian)
- [❓ FAQ](#-faq)
- [📄 License](#-license)

---

## ✨ Features

- 🔄 **Auto-Reconnect Loop**: Continuously checks voice connection status every 10 seconds and automatically reconnects if dropped.
- 🔇 **Zero-Bandwidth Idling**: Automatically mutes and deafens itself upon joining to minimize bandwidth and CPU usage.
- 🛠️ **Self-Healing**: Recovers gracefully from network interruptions, server restarts, or manual disconnects.
- 🔒 **Secure Configuration**: Uses environment variables (`.env`) so your secret tokens remain safe.

---

## 📖 Step-by-Step Setup Guide

### Step 1: Get Discord Credentials
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application**, enter a name (e.g., `CallKeeper`), and click **Create**.
3. In the left sidebar, click **Bot**.
4. Click **Reset Token**, copy the generated token, and save it somewhere safe. *(This is your `DISCORD_TOKEN`)*.
5. Get your **Voice Channel ID**:
   - Open Discord -> **User Settings** -> **Advanced** -> Turn ON **Developer Mode**.
   - Right-click the voice channel you want the bot to join and click **Copy Channel ID**. *(This is your `VOICE_CHANNEL_ID`)*.

---

### Step 2: Invite Bot to Server
1. In the Developer Portal, go to **OAuth2** -> **URL Generator**.
2. Under **Scopes**, check `bot`.
3. Under **Bot Permissions**, check:
   - `Connect` (Voice Permissions)
   - `Speak` (Voice Permissions)
4. Copy the generated URL at the bottom, paste it into your browser, select your server, and click **Authorize**.

---

### Step 3: Local Installation
Open your terminal or command prompt and clone the repository:

```bash
# 1. Clone the repository
git clone https://github.com/WspJon/CallKeeper.git
cd CallKeeper

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# Windows (PowerShell):
.\venv\Scripts\activate
# Windows (CMD):
.\venv\Scripts\activate.bat
# macOS / Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
```

---

### Step 4: Configure Credentials
You need to create your secret `.env` file from the sample template:

- **Via Terminal / Command Prompt:**
  ```bash
  # Windows (PowerShell) or Linux/macOS:
  cp .env.example .env

  # Windows (CMD):
  copy .env.example .env
  ```
- **Via File Explorer:**
  Simply right-click `.env.example`, select **Copy**, paste it into the same folder, and rename the copy to `.env`.

Open `.env` in any text editor and paste your credentials:
```env
DISCORD_TOKEN=your_actual_bot_token_here
VOICE_CHANNEL_ID=your_voice_channel_id_here
```

---

### Step 5: Run the Bot
```bash
python bot.py
```
You will see output indicating the bot has successfully logged in and joined the voice channel!

---

## 🌐 24/7 Hosting Guide (Run Without PC On)

If you want the bot to stay in the call 24/7 even when your PC is turned off, you can deploy it to a free cloud service or a Linux VPS.

---

### Option A: Free Hosting on Render.com (Recommended)

1. Push your code to your GitHub repository ([WspJon/CallKeeper](https://github.com/WspJon/CallKeeper)).
2. Sign up for a free account at [Render.com](https://render.com/).
3. On your Render Dashboard, click **New +** -> **Background Worker**.
4. Connect your GitHub account and select your **`CallKeeper`** repository.
5. Fill in the deployment details:
   - **Name**: `callkeeper-bot`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
6. Scroll down to **Environment Variables** and add two variables:
   - Key: `DISCORD_TOKEN` | Value: *(Your bot token)*
   - Key: `VOICE_CHANNEL_ID` | Value: *(Your voice channel ID)*
7. Click **Create Background Worker**.

> Render will automatically build and run your bot 24/7 in the cloud for free!

---

### Option B: VPS / Linux Server (Ubuntu/Debian)

If you have a Linux VPS (e.g., DigitalOcean, AWS, Linode), you can use `pm2` to keep the bot running indefinitely:

```bash
# 1. Update system & install Node.js + PM2 + Python
sudo apt update && sudo apt install -y python3 python3-pip python3-venv nodejs npm
sudo npm install -g pm2

# 2. Clone repository & setup
git clone https://github.com/WspJon/CallKeeper.git
cd CallKeeper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Create .env file with your credentials
nano .env

# 4. Start bot using PM2
pm2 start bot.py --name "callkeeper" --interpreter ./venv/bin/python

# 5. Enable PM2 to auto-restart on server reboot
pm2 startup
pm2 save
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
