import os
from distutils.dir_util import copy_tree

from threading import Thread


class Bot:
    def __init__(self, bot_token) -> None:
        self.bot_token = bot_token
        self.path_name = f"bot/user_bots/{bot_token.split(':')[0]}"


    def start_thread(self, template):
        if not os.path.isdir(self.path_name):
            self._make_dir()
            copy_tree(f"bot/bot_templates/{template}", self.path_name)

        new_bot = Thread(target=self._start_bot)
        new_bot.start()


    def kill_thread(self):
        pass


    def _make_dir(self):
        os.mkdir(self.path_name)


    def _start_bot(self):
        print(f"{self.bot_token=}")
        os.system(f"python {self.path_name}/main.py {self.bot_token}")
        print("Поток закрыт")
