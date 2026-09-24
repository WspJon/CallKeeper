import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import tasks

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
VOICE_CHANNEL_ID = os.getenv('VOICE_CHANNEL_ID')

if not TOKEN or not VOICE_CHANNEL_ID:
    print("Error: DISCORD_TOKEN and VOICE_CHANNEL_ID must be set in the .env file.")
    exit(1)

try:
    VOICE_CHANNEL_ID = int(VOICE_CHANNEL_ID)
except ValueError:
    print("Error: VOICE_CHANNEL_ID must be a valid integer.")
    exit(1)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    # Start the background loop to ensure it stays connected
    if not ensure_voice_connection.is_running():
        ensure_voice_connection.start()

@tasks.loop(seconds=10)
async def ensure_voice_connection():
    """A background task that runs every 10 seconds to make sure the bot is in the VC"""
    try:
        channel = client.get_channel(VOICE_CHANNEL_ID)
        if not channel:
            print(f"Error: Could not find voice channel with ID {VOICE_CHANNEL_ID}")
            return
            
        if not isinstance(channel, discord.VoiceChannel):
            print(f"Error: The provided ID is not a Voice Channel. It is a {type(channel)}")
            return

        # Check if the bot is currently in a voice channel in this server
        vc = discord.utils.get(client.voice_clients, guild=channel.guild)
        
        # If not connected at all, or connected to the wrong channel
        if vc is None or not vc.is_connected():
            print(f"Bot is not in the channel. Attempting to connect to {channel.name}...")
            # Clean up old connection state if it got stuck
            if vc is not None:
                await vc.disconnect(force=True)
                
            vc = await channel.connect()
            print(f"Successfully connected to {channel.name}")
            # Keep bot deafened to save bandwidth
            await vc.guild.change_voice_state(channel=channel, self_mute=True, self_deaf=True)
            
        elif vc.channel.id != VOICE_CHANNEL_ID:
            print(f"Bot is in the wrong channel. Moving to {channel.name}...")
            await vc.move_to(channel)
            await vc.guild.change_voice_state(channel=channel, self_mute=True, self_deaf=True)
            
    except Exception as e:
        print(f"Error in background connection task: {e}")

@ensure_voice_connection.before_loop
async def before_ensure_voice_connection():
    # Wait until the bot is fully ready before starting the loop
    await client.wait_until_ready()

if __name__ == "__main__":
    client.run(TOKEN)
