import os
from distutils.dir_util import copy_tree

from threading import Thread


class Bot:
    def __init__(self, bot_token) -> None:
        self.bot_token = bot_token
        self.path_name = f"bot/user_bots/{bot_token.split(':')[0]}"
        print(self.path_name)
        os.mkdir(self.path_name)


    def start_thread(self, template):
        print('start_thread')
        copy_tree(f"bot/bot_templates/{template}", self.path_name)
        new_bot = Thread(target=self._start_bot)
        new_bot.start()

    def _start_bot(self):
        print(f"{self.bot_token=}")
        os.system(f"python {self.path_name}/main.py {self.bot_token}")
        print("Поток закрыт")
