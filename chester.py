import berserk
import discord
import os
import sys

from dotenv import load_dotenv

load_dotenv()


class Chester(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        self.session = berserk.TokenSession(os.environ.get('LICHESS_API_TOKEN'))
        self.lichess = berserk.Client(self.session)

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        message_tokens = message.content.strip().split()
        prefix_token = message_tokens.pop(0)

        if prefix_token == '!lichess':
            response = os.environ.get('FALLBACK_RESPONSE')

            if message_tokens[0] == 'profile':
                try:
                    response_body = self.lichess.users.get_public_data(message_tokens[1])
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
