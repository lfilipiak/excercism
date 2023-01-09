def rotate(text: str, key: int) -> str:
    sentence = ""

    for char in text:
        if 65 > ord(char) > 90 or 97 > ord(char) < 122:
            sentence = sentence + char
            continue
        else:
            sentence = sentence + "".join(chr(ord(char) + key % 26))
        # sentence = sentence + "".join(chr(ord(char) + key % 26))

    return sentence


print(rotate("ASD", 10))
