def say(number):

    sentence = ""
    list_of_ints = [x for x in str(number)]
    len_of_number = len(list_of_ints)

    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    translate = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        20: "twenty",
        30: "thirty",
        50: "fifty",
        100: "hundred",
        1_000: "thousand",
        1_000_000: "million",
        1_000_000_000: "billion",
    }

    if number <= 13:
        return translate[number]
    elif number >= 14 and number <= 19 and number != 15 and number != 18:
        return f"{translate[number-10]}teen"
    elif number == 15:
        return "fifteen"
    elif number == 18:
        return "eighteen"

    if len_of_number >= 10:
        sentence = f"{translate[int(list_of_ints[0])]}"
    return sentence


print(say(2233123123))
