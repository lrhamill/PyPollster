import uuid
from poll_option import PollOption


class Poll:

    def __init__(self, name: str):

        self.name = name
        self.id = str(uuid.uuid4()).replace("-", "")
        self.poll_options = []

    def add_option(self, option: PollOption):
        self.poll_options.append(option)

    def add_options_from_list(self, option_list: list):
        self.poll_options += option_list
