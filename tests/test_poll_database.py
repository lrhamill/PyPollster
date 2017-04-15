import unittest
from poll_database import PollDatabase
from poll import Poll


class TestPollDatabase(unittest.TestCase):

    def setUp(self):

        self.reader = PollDatabase(":memory:")
        self.reader.new_db()

    def tearDown(self):

        self.reader.close()

    def test_get_polls_with_name_does_not_exist_returns_empty_list(self):

        output = self.reader.get_polls_with_name("poll")

        self.assertEqual(len(output), 0)

    def test_get_polls_name_exists_returns_poll(self):

        self.reader.add_poll(Poll("poll"))
        output = self.reader.get_polls_with_name("poll")

        self.assertEqual(len(output), 1)
        self.assertTrue(output[0].name == "poll")

if __name__ == '__main__':
    unittest.main()
