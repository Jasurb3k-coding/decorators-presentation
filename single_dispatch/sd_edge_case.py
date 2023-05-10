from functools import singledispatch


@singledispatch
def add(a, b):
    print(a, b)


@add.register
def add_numbers(a: int, b: int):
    return "int int"


@add.register
def add_numbers(a: int, b: str):
    return "int str"


@add.register
def add_numbers(a: str, b: int):
    return "str int"


@add.register
def add_numbers(a: str, b: str):
    return "str str"


if __name__ == '__main__':
    print(add(1, 1))
