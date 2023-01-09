PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = PLAIN[::-1]


def encode(plain_text: str):
    return "".join(plain_text.split(" "))


def decode(ciphered_text):
    pass


print(encode("abcdefga sd asddd asd asda asd s"))