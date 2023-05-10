import status_update
from functools import singledispatchmethod


class Listener:
    @singledispatchmethod
    def process(self, event: status_update.StatusUpdate) -> None:
        raise NotImplementedError(f'type {type(event)} is not supported')

    @process.register
    def paid_in_full(self, event: status_update.PaidInFull):
        """
        SOME LONG LOGIC
        """
        print(f"PAID IN FULL: {event}")

    @process.register
    def paid_in_part(self, event: status_update.PaidInPart):
        """
        SOME LONG LOGIC
        """
        print(f"PAID IN PART: {event}")

    @process.register
    def paid_in_part(self, event: status_update.DeclaredBankruptcy):
        """
        SOME LONG LOGIC
        """
        print(f"Declared Bankruptcy: {event}")

    @process.register
    def paid_in_part(self, event: status_update.SavingFailed):
        """
        SOME LONG LOGIC
        """
        print(f"Saving Failed: {event}")


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
