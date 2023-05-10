from exception import NoLinkError, NoSpeakerError, NoNumberOfAttendanceError


class MeetUp:
    def __init__(self, event_id, event_title, speaker,
                 number_of_attendance, link):
        if not speaker:
            raise NoSpeakerError
        if not link:
            raise NoLinkError
        if not number_of_attendance:
            raise NoNumberOfAttendanceError
        self.event_id = event_id
        self.event_title = event_title
        self.speaker = speaker
        self.number_of_attendance = number_of_attendance
        self.link = link
