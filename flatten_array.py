x = [1, 2, None]


def flatten(iterable):

    flist = []
    flist.extend ([iterable]) if (type (iterable) is not list) else [flist.extend (flatten (e)) for e in iterable]
    for x in flist:
        if x == None:
            flist.pop(flist.index(x))
    return flist


print(flatten(x))
