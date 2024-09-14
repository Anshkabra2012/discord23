import os
import discord
from discord.ext import commands

# Set up the bot with a command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: When the bot is ready and connected
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Event: Respond to a specific user
@bot.event
async def on_message(message):
    if message.author.id == 1039270270101356664:  # Replace with the target user ID
        await message.channel.send("No way roblox player is talking")
    await bot.process_commands(message)

# Get the token from the environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Run the bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_BOT_TOKEN environment variable not found.")
