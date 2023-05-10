import status_update


class Listener:
    def process(self, event: status_update.StatusUpdate) -> None:
        if isinstance(event, status_update.PaidInFull):
            self.on_paid_in_full(event)
        elif isinstance(event, status_update.PaidInPart):
            self.on_paid_in_part(event)
        elif isinstance(event, status_update.DeclaredBankruptcy):
            self.on_declared_bankruptcy(event)
        elif isinstance(event, status_update.SavingFailed):
            raise TypeError(f'{type(event)} is not supported')

    def on_success(self, event):
        """
        SOME LONG LOGIC
        """
        print(f"SUCCESS: {event}")

    def on_fail(self, event):
        """
        SOME LONG LOGIC
        """
        print(f"FAIL: {event}")

    def on_paid_in_full(self, event):
        """
        SOME LONG LOGIC
        """
        print(f"{event.code = }")

    def on_paid_in_part(self, event):
        """
        SOME LONG LOGIC
        """
        print(f"{event.code = }")

    def on_declared_bankruptcy(self, event):
        """
        SOME LONG LOGIC
        """
        print(f"{event.code = }")

    def on_saving_failed(self, event):
        """
        SOME LONG LOGIC
        """
        print(f"{event.code = }")


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
