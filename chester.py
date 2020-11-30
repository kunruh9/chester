import discord


class Chester(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'yohomie':
            await message.channel.send('SUP BRO')


chester = Chester()
chester.run('Nzc4NDkxNTExMDcwMzkyMzIx.X7Swtw.DMZ97f6t_4eZBF7K5-5XMwHj56c')
