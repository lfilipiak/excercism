def label(colors: list) -> str:

    bands = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    value = (bands[colors[0]] * 10 + bands[colors[1]]) * (
        10 ** bands[colors[2]]
    )  # noqa: 501
    if value > 1000:
        value = value // 1000
        return f"{value} kiloohms"
    return f"{value} ohms"
