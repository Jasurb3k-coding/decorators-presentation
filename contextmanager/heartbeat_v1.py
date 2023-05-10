import time
from contextmanager.lib import count_to_n_generate, count_to_n_list


def send_heart_beat(n: int):
    print(f"Sent Heartbeat at {n}")


if __name__ == '__main__':
    """
    requirement:
        - count till 300
            - in every 50 nums send a heartbeat
    """
    print(f'{count_to_n_list(300) = }')
