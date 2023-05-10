import status_update


if __name__ == '__main__':
    """
    Implement Listener
    Implement Listener.process
    """
    listener = Listener()

    update1 = status_update.PaidInPart(
        user_id='1',
        loan_id='1',
    )

    update2 = status_update.PaidInPart(
        user_id='1',
        loan_id='1',
    )

    listener.process(update1)
    listener.process(update2)
