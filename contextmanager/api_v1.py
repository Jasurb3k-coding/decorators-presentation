class API:
    def run_this_first(self):
        print("Running first")

    def run_this_second(self):
        print("Running second")

    def run_this_last(self):
        print("Running last")



if __name__ == '__main__':
    API().run_this_last()
    API().run_this_second()
    API().run_this_first()

    # API().run_this_first()
    # "Do something"
    # API().run_this_second()
    # "Do something"
    # API().run_this_last()
