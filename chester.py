import discord
import os

from dotenv import load_dotenv
load_dotenv()


class Chester(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'yohomie':
            await message.channel.send('SUP BRO')


chester = Chester()
chester.run(os.environ.get('CHESTER_TOKEN'))
