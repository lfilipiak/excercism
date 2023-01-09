import itertools


def append(list1: list, list2: list):
    return list1 + list2


def concat(lists: list):
    return list(itertools.chain(*lists))


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    return sum(item for item in list) + initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(item, initial)
    return initial


def reverse(list):
    return list[::-1]
