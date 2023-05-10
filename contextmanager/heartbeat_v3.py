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
    gen = count_to_n_generate(300)
    for num in gen:
        print(num)
        if num == 200:
            break
    """LOGIC"""

    print("IDLE...")
    time.sleep(4)
    for num in gen:
        print(num)
