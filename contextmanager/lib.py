import time


def count_to_n_list(n: int):
    ls_of_items = []
    for i in range(n):
        time.sleep(0.01)
        ls_of_items.append(i + 1)
    return ls_of_items


def count_to_n_generate(n: int):
    for i in range(n):
        time.sleep(0.01)
        yield i + 1
