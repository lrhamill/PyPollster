import uuid


class PollOption:

    def __init__(self, name: str):

        self.name = name
        self.id = str(uuid.uuid4()).replace("-", "")
