import uuid


class PollOption:

    def __init__(self, name: str):

        self.name = name
        self.id = uuid.uuid4().int
