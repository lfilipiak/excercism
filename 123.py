def spin_words(sentence:str):

    sentence = sentence.split(" ")
    for index, word in enumerate(sentence):
        if len(word) >= 5:
            sentence[index] = word[::-1]

    return " ".join(sentence)


print(spin_words("Hey fellow warriors"))