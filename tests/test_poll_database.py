import unittest
from poll_database import PollDatabase
from poll import Poll
from poll_option import PollOption


class TestPollDatabase(unittest.TestCase):

    def setUp(self):

        self.db = PollDatabase(":memory:")
        self.db.new_db()

    def tearDown(self):

        self.db.close()

    def test_get_polls_with_name_does_not_exist_returns_empty_list(self):

        output = self.db.get_polls_with_name("poll")
        self.assertEqual(len(output), 0)

    def test_get_polls_name_exists_returns_poll(self):

        self.db.add_poll(Poll("poll"))
        output = self.db.get_polls_with_name("poll")

        self.assertEqual(len(output), 1)
        self.assertTrue(output[0].name == "poll")

    def test_get_polls_ID_values_match_as_expected(self):
        test_poll = Poll("poll")
        self.db.add_poll(test_poll)
        output = self.db.get_polls_with_name("poll")

        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].id, test_poll.id)

    def test_get_polls_with_options_returns_poll_with_correct_options(self):

        test_poll = Poll("options_test")
        test_poll.add_options_from_list([PollOption("first"), PollOption("second"), PollOption("third")])

        test_poll2 = Poll("second_test")
        test_poll2.add_options_from_list([PollOption("fourth"), PollOption("fifth"), PollOption("sixth")])

        self.db.add_poll(test_poll)
        self.db.add_poll(test_poll2)

        output = self.db.get_polls_with_name("options_test")
        self.assertEqual(len(output), 1)
        self.assertEqual(len(output[0].poll_options), len(test_poll.poll_options))
        for actual, expected in zip(output[0].poll_options, test_poll.poll_options):
            self.assertEqual(actual.name, expected.name)

        output = self.db.get_polls_with_name("second_test")
        self.assertEqual(len(output), 1)
        self.assertEqual(len(output[0].poll_options), len(test_poll2.poll_options))
        for actual, expected in zip(output[0].poll_options, test_poll2.poll_options):
            self.assertEqual(actual.name, expected.name)

if __name__ == '__main__':
    unittest.main()
