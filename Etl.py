def transform(legacy_data):
    list = []
    value = {}

    for x in legacy_data.values():
        list.extend(x)

    list.sort()

    for element in list:
        x = []
        x = [k for k, v in legacy_data.items() if element in v]
        value.update({element.lower(): x[0]})

    return value
