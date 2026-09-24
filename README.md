# 🎙️ CallKeeper

A simple 24/7 Discord bot that stays in a voice channel to keep the call timer running. It automatically reconnects if kicked or disconnected.

---

## ⚡ Quick Setup

### 1. Get Discord Tokens
- Go to [Discord Developer Portal](https://discord.com/developers/applications) -> Create an App -> **Bot** tab -> Click **Reset Token** and copy it.
- Open Discord -> **Settings** -> **Advanced** -> Turn ON **Developer Mode**.
- Right-click your voice channel -> **Copy Channel ID**.

### 2. Invite Bot to Server
- In Developer Portal: **OAuth2** -> **URL Generator**.
- Select **`bot`** scope and **`Connect`** permission.
- Copy the generated link, open it in your browser, and select your server.

### 3. Install & Configure
1. Clone this repository:
   ```bash
   git clone https://github.com/WspJon/CallKeeper.git
   cd CallKeeper
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Make a copy of `.env.example` and name it `.env`.
4. Open `.env` and paste your credentials:
   ```env
   DISCORD_TOKEN=your_token_here
   VOICE_CHANNEL_ID=your_voice_channel_id_here
   ```

### 4. Run the Bot
```bash
python bot.py
```

---

## 🌐 Free 24/7 Hosting (Render.com)

To keep it running even when your PC is off:

1. Go to [Render.com](https://render.com/) and sign up.
2. Click **New +** -> **Background Worker** -> Connect your GitHub repo `CallKeeper`.
3. Set **Start Command**: `python bot.py`
4. Add Environment Variables:
   - `DISCORD_TOKEN` = *(Your token)*
   - `VOICE_CHANNEL_ID` = *(Your voice channel ID)*
5. Click **Create Background Worker**. Done!

---

## 📄 License
MIT
