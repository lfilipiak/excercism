x = [2, 2, [123, [334]], 34, [], 123, []]

value = []


def flatten(iterable: list):

    if len(iterable) != 0:
        if iterable[0] is not None:
            if type(iterable[0]) is not type([]):
                value.append(iterable[0])
                iterable.pop(0)
                return flatten(iterable)
            else:
                return flatten(iterable[0])
        else:
            iterable.pop(0)
            return flatten(iterable)
    else:
        return value


print(flatten(iterable=x))
