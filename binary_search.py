def find(search_list: list, value: int):
    try:
        return search_list.index(value)
    except ValueError:
        raise ValueError("value not in array")
