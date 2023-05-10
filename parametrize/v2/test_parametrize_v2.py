from parametrize.v2.main import MeetUp

from exception import NoLinkError, NoSpeakerError, NoNumberOfAttendanceError

import pytest


class TestParametrize:
    @pytest.mark.parametrize("overrides,expected_error", [
        ({'speaker': None}, NoSpeakerError),  # Test Case 1
        ({'number_of_attendance': None}, NoNumberOfAttendanceError),  # Test Case 2
        ({'link': None}, NoLinkError),  # Test Case 3
    ])
    def test_meetup_dto(self, overrides, expected_error):
        with pytest.raises(expected_error):
            self.get_mock_event(overrides)

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

        return MeetUp(
            event_id=event_id,
            event_title=event_title,
            speaker=speaker,
            number_of_attendance=number_of_attendance,
            link=link
        )
