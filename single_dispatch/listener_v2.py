import status_update


class Listener:
    def process(self, event: status_update.StatusUpdate) -> None:
        if isinstance(event, status_update.PaidInFull):
            """
            SOME LONG LOGIC
            """
            print(f"{event.code = }")
        elif isinstance(event, status_update.PaidInPart):
            """
            SOME LONG LOGIC
            """
            print(f"{event.code = }")
        elif isinstance(event, status_update.DeclaredBankruptcy):
            """
            SOME LONG LOGIC
            """
            print(f"{event.code = }")
        elif isinstance(event, status_update.SavingFailed):
            """
            SOME LONG LOGIC
            """
            print(f"{event.code = }")
        elif isinstance(event, status_update.SavingFailed):
            raise TypeError(f'{type(event)} is not supported')


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
