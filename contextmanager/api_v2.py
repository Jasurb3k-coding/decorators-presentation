def api():
    print("Running first")
    yield
    print("Running second")
    yield
    print("Running last")


if __name__ == '__main__':
    gen = api()
    next(gen, None)
    next(gen, None)
    next(gen, None)
