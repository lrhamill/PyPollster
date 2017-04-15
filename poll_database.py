import sqlite3
from poll import Poll
from poll_option import PollOption


class PollDatabase:
    # TODO make this more generic

    def __init__(self, sqlite_filename):

        self.conn = sqlite3.connect(sqlite_filename)
        self.cursor = self.conn.cursor()

    def new_db(self):

        self.cursor.execute("CREATE TABLE polls (name TEXT, id TEXT PRIMARY KEY)")
        self.cursor.execute("CREATE TABLE options (name TEXT, poll TEXT, id TEXT PRIMARY KEY)")
        self.conn.commit()

    def add_poll(self, poll: Poll):

        self.cursor.execute('INSERT INTO polls (name, id) VALUES ("{}", {})'
                            .format(poll.name, poll.id))

        for option in poll.poll_options:
            self.cursor.execute('INSERT INTO options (name, poll, id) VALUES ("{}", {}, {})'
                                .format(option.name, poll.id, option.id))

        self.conn.commit()

    def get_poll_options_for_poll(self, poll: Poll):

        try:
            self.cursor.execute('SELECT name, id FROM options WHERE poll="{}"'.format(poll.id))
            db_options = self.cursor.fetchall()

        except sqlite3.OperationalError:
            return []

        retrieved_options = [PollOption(option[0]) for option in db_options]

        for new_option, db_option in zip(retrieved_options, db_options):
            new_option.id = db_option[1]

        return retrieved_options

    def get_polls_with_name(self, name: str) -> list:

        try:
            self.cursor.execute('SELECT * FROM polls WHERE name="{}"'.format(name))
            db_polls = self.cursor.fetchall()

        except sqlite3.OperationalError:
            return []

        retrieved_polls = [Poll(poll_fields[0]) for poll_fields in db_polls]
        zipped = zip(retrieved_polls, db_polls)
        for new_poll, db_poll in zip(retrieved_polls, db_polls):
            new_poll.id = db_poll[1]

        for poll in retrieved_polls:
            poll.add_options_from_list(self.get_poll_options_for_poll(poll))

        return retrieved_polls

    def close(self):

        self.conn.close()
