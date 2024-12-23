class NewClass(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


if __name__ == "__main__":
    obj = NewClass("test")
    print(obj)
