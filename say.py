import logging as log

log.basicConfig(level=log.DEBUG, format="%(message)s")


def say(number):

    sentence = ""
    tens_flag = True
    hundreds_flag = True
    list_of_digits = [x for x in str(number)]
    len_of_number = len(list_of_digits)
    chunks_value = (len_of_number - 1) // 3

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

    # chunks = {
    #     0: "hundred",
    #     1: "thousand",
    #     2: "million",
    #     3: "billion",
    # }

    list_of_digits.reverse()

    while list_of_digits:
        if tens_flag:
            x = "".join(list_of_digits[0:2])
            if number <= 13:
                sentence +=
                # return translate[number]
            elif number >= 14 and number <= 19 and number != 15 and number != 18:
                # return f"{translate[number-10]}teen"
            elif number == 15:
                # return "fifteen"
            elif number == 18:
                # return "eighteen"
            elif number in translate.keys():
                # return translate[number]
            tens_flag = False
            list_of_digits.pop(0)
            list_of_digits.pop(0)
            log.info(list_of_digits)
            log.info(x)
        if hundreds_flag:

    
    log.info(len_of_number)

    return sentence

    

    # if number >= 21:
    #     for digit in list_of_digits:
    #         if len_of_number < 3:
    #             sentence += f"{translate[int(list_of_digits[0])]}"

    #         log.info(chunks[chunks_value])
    #         log.info(sentence)
    # return sentence


print(say(123456789012))
