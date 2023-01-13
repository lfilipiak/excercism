PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = PLAIN[::-1]


def encode(plain_text: str):
    encode_text = []
    tmp = []
    text = "".join(plain_text.split(" ")).lower()
    for letter in text:
        if letter.isdecimal():
            tmp.append(letter)
            if len(tmp) == 5:
                encode_text.extend(tmp)
                encode_text.append(" ")
                tmp.clear()
            continue
        if not letter.isalnum():
            continue
        tmp.append(CIPHER[PLAIN.index(letter)])
        if len(tmp) == 5:
            encode_text.extend(tmp)
            encode_text.append(" ")
            tmp.clear()
    encode_text.extend(tmp)
    if len(text) < 5:
        return "".join(tmp)
    return "".join(encode_text).lstrip(" ").rstrip(" ")


def decode(ciphered_text):
    decode_text = []
    text = ciphered_text.replace(" ", "")
    for letter in text:
        if letter.isdecimal():
            decode_text.append(letter)
            continue
        decode_text.append(PLAIN[CIPHER.index(letter)])
    return "".join(decode_text)


print(decode("vcvix rhn"))
