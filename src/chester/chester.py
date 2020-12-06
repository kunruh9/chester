import discord
import sys

from src.clients.lichess import *

lichess = LiChess()
COMMAND_PREFIX = '!lichess'


class Chester(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if not message.content.startswith(COMMAND_PREFIX):
            return

        message_tokens = message.content.strip().lstrip(COMMAND_PREFIX).split()

        if len(message_tokens) < 1:
            return

        response = os.environ.get('FALLBACK_RESPONSE')

        if message_tokens[0] == 'profile':
            try:
                if len(message_tokens) < 2:
                    return

                response_body = lichess.users.get_public_data(message_tokens[1])
                self.calculate_games_played(response_body)
                response = '''`{username}`
                **Games Played:** {games_played}
                **Online?:** {online}
                '''.format(**response_body)
            except berserk.exceptions.ResponseError as e:
                if e.status_code == 404:
                    response = f'`{message_tokens[1]}` not found :('

        await message.channel.send(response)

    async def on_error(self, event_method, *args, **kwargs):
        print(sys.exc_info())
        await args[0].channel.send(os.environ.get('ERROR_RESPONSE'))

    @staticmethod
    def calculate_games_played(response_body):
        total = 0
        for game_stats in response_body['perfs'].items():
            total += game_stats[1].get('games', 0)

        response_body['games_played'] = total


chester = Chester()
chester.run(os.environ.get('CHESTER_TOKEN'))
