from events import SuccessEvent, FailEvent, BaseEvent
import status_update
from functools import singledispatchmethod


class Listener:
    @singledispatchmethod
    def process(self, event: BaseEvent):
        print(f"{type(event)} is not supported")

    @process.register
    def process_success(self, event: SuccessEvent):
        """
        SOME LONG LOGIC
        """
        print(f"SUCCESS: {event}")

    @process.register
    def process_fail(self, event: FailEvent):
        """
        SOME LONG LOGIC
        """
        print(f"FAIL: {event}")


if __name__ == '__main__':
    listener = Listener()

    update1 = status_update.PaidInPart(
        user_id='1',
        loan_id='1',
    )

    update2 = status_update.PaidInFull(
        user_id='1',
        loan_id='1',
    )

    listener.process(update1)
    listener.process(update2)
