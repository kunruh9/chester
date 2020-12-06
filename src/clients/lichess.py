import berserk
import os

from dotenv import load_dotenv

load_dotenv()


class LiChess(berserk.Client):
    def __init__(self, **options):
        session = berserk.TokenSession(os.environ.get('LICHESS_API_TOKEN'))
        super().__init__(session, **options)
