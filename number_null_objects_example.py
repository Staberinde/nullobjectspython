from optional import optional_of_nullable, optional_of, empty


def product(x, y):
    if x is None or y is None:
        return 0
    else:
        return x * y


def sum(x, y):
    return (x or 0) + (y or 0)
