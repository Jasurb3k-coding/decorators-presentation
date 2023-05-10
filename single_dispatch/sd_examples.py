from functools import singledispatch


@singledispatch
def serialize(data):
    print("Invalid Object")


@serialize.register
def serialize_list(data: list):
    print("Serializing list")


@serialize.register
def serialize_object(data: dict):
    print("Serializing Single Object")


if __name__ == '__main__':
    data_list = [{'id': 1}]
    data_item = {'id': 2}

    serialize(data_list)
    serialize(data_item)
    serialize(5)
    serialize("AS")
