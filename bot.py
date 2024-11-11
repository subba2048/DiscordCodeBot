import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
token = os.getenv('DISCORD_TOKEN')
client.run(token)  # Use the token from the .env file