import os
import requests

from distutils.dir_util import copy_tree
from threading import Thread


class Bot:
    def __init__(self, bot_token) -> None:
        self.bot_token = bot_token
        self.path_name = f"bot/user_bots/{bot_token.split(':')[0]}"


    def start_thread(self, template):
        self._check_dir(template)

        new_bot = Thread(target=self._start_bot)
        new_bot.start()


    def _check_dir(self, template):
        if not os.path.isdir(self.path_name):
            self._make_dir()
            copy_tree(f"bot/bot_templates/{template}", self.path_name)

    def _make_dir(self):
        os.mkdir(self.path_name)

    def _start_bot(self):
        print(f"{self.bot_token=}")
        os.system(f"python {self.path_name}/main.py {self.bot_token}")
        print("Поток закрыт")


    def get_bot_info(self):
        bot_info = requests.get(f"https://api.telegram.org/bot{self.bot_token}/getMe").json()['result']
        print(f'{bot_info=}')
        bot_name = bot_info['first_name']
        bot_username = bot_info['username']

        return bot_name, bot_username