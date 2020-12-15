from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()


with open_file("nameslist.txt", "r") as file:
    names = file.read().split("\n")
    print({i: names.count(i) for i in names})
