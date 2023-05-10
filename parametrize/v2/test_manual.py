import unittest

from parametrize.v2.main import MeetUp
from exception import NoLinkError, NoSpeakerError, NoNumberOfAttendanceError


class TestManual(unittest.TestCase):

    def test_meetup_all_provided(self):
        # Test Case 1: Event with all fields provided
        meetup = self.get_mock_event()

    def test_meetup_no_speaker(self):
        # Test Case 2: Event with speaker set to None
        self.assertRaises(NoSpeakerError, self.get_mock_event, {'speaker': None})

    def test_meetup_no_number_of_attendance(self):
        # Test Case 3: Event with number_of_attendance set to None
        self.get_mock_event({'number_of_attendance': None})

    def test_meetup_no_link(self):
        self.assertRaises(NoLinkError, self.get_mock_event, {'link': None})

    def test_meetup_no_number_of_attendance(self):
        self.assertRaises(NoNumberOfAttendanceError, self.get_mock_event, {'number_of_attendance': None})

    def get_mock_event(self, overrides=None):
        if overrides is None:
            overrides = {}
        data = {
            'event_id': 1,
            'event_title': "Python Meetup",
            'speaker': "John Doe",
            'number_of_attendance': 50,
            'link': "https://example.com/meetup1"
        }
        data.update(overrides)
        event_id, event_title, speaker, number_of_attendance, link = data.values()

        return MeetUp(event_id=event_id, event_title=event_title, speaker=speaker,
                      number_of_attendance=number_of_attendance, link=link)
