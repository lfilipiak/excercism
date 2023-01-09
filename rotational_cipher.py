def rotate(text: str, key: int) -> str:
    sentence = ""

    for char in text:

        if (ord(char) >= 65 and ord(char) <= 90) or (
            ord(char) >= 97 and ord(char) <= 122
        ):
            if ord(char) >= 97:
                if ord(char) + key % 26 not in range(97, 123, 1):
                    sentence = sentence + "".join(
                        chr(ord(char) + key % 26 - ord("z") + ord("a") - 1)
                    )
                else:
                    sentence = sentence + "".join(chr(ord(char) + key % 26))
            else:
                if ord(char) + key % 26 not in range(65, 91, 1):
                    sentence = sentence + "".join(
                        chr(ord(char) + key % 26 - ord("Z") + ord("A") - 1)
                    )
                else:
                    sentence = sentence + "".join(chr(ord(char) + key % 26))
        else:
            sentence = sentence + char
            continue

    return sentence


print(rotate("ABC BCA ZZZ AAA zzz aaa '''", 36))
