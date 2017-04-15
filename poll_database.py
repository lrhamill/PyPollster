import sqlite3
from poll import Poll


class PollDatabase:

    def __init__(self, sqlite_filename):

        self.conn = sqlite3.connect(sqlite_filename)
        self.cursor = self.conn.cursor()

    def new_db(self):

        self.cursor.execute("CREATE TABLE polls (name TEXT)")
        self.conn.commit()

    def add_poll(self, poll: Poll):

        self.cursor.execute('INSERT INTO polls (name) VALUES ("{}")'.format(poll.name))
        self.conn.commit()

    def get_polls_with_name(self, name: str) -> list:

        try:

            self.cursor.execute('SELECT * FROM polls WHERE name="{}"'.format(name))
            polls = self.cursor.fetchall()

        except sqlite3.OperationalError:

            return []

        return [Poll(*poll_fields) for poll_fields in polls]

    def close(self):

        self.conn.close()