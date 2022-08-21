def commands(binary_str: str) -> list:
    value = []
    handshake = ["wink", "double blink", "close your eyes", "jump"]

    for i, j in enumerate(binary_str[:0:-1]):
        print(i, j)
        if j == "1":
            value.append(handshake[i])
            print(value)

    if binary_str[0] == "1":
        value.reverse()
    return value


print(commands("10011"))
