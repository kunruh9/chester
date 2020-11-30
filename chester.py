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
# TODO: Update this token with the new one since I accidentally uploaded this one :facepalm:
chester.run('Nzc4NDkxNTExMDcwMzkyMzIx.X7Swtw.DMZ97f6t_4eZBF7K5-5XMwHj56c')

# notes on where I left off:
# - Figuring out the best way/convention for interacting with environment variables in python
# - Once that is figured out, I can set my token in the environment, and reference it above.
# - Then I will be able to continue with the heroku "getting started" tutorial:
#   - https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app
