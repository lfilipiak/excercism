"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):

    value = {"A": 1, "J": 10, "Q": 10, "K": 10}

    if card.isdigit():
        return int(card)
    else:
        return value[card]

    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    pass


def higher_card(card_one:str, card_two:str):

    value = {"A": 1, "J": 10, "Q": 10, "K": 10}

    if card_one.isdigit():
        digit_card_one=int(card_one)
    else:
        digit_card_one=value[card_one]

    if card_two.isdigit():
        digit_card_two=int(card_two)
    else:
        digit_card_two=value[card_two]

    if digit_card_one > digit_card_two:
        return card_one
    elif digit_card_one < digit_card_two:
        return card_two
    else:
        return (card_one, card_two)    

print(higher_card('K', 'Q'))



def value_of_ace(card_one, card_two):

    value = {"A": 11, "J": 10, "Q": 10, "K": 10}
    if card_one.isdigit():
        card_one = int(card_one)
    else:
        card_one = value[card_one]

    
    if card_two.isdigit():
        card_two = int(card_two)
    else:
        card_two = value[card_two]

    
    if card_one + card_two >= 11:
        return 1
    else:
        if "A" in (card_one, card_two):
            return 1
        else:
            return 11


def is_blackjack(card_one, card_two):
    if card_one == card_two:
        return False

    value = {"A": 11, "J": 10, "Q": 10, "K": 10}
    
    if card_one.isdigit():
        card_one = int(card_one)
    else:
        card_one = value[card_one]

    
    if card_two.isdigit():
        card_two = int(card_two)
    else:
        card_two = value[card_two]

    if card_one + card_two == 21:
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    value = {"A": 11, "J": 10, "Q": 10, "K": 10}
    
    if card_one.isdigit():
        card_one = int(card_one)
    else:
        card_one = value[card_one]

    
    if card_two.isdigit():
        card_two = int(card_two)
    else:
        card_two = value[card_two]

    if card_one == card_two:
        return True
    else: 
        return False

def can_double_down(card_one, card_two):
    value = {"A": 1, "J": 10, "Q": 10, "K": 10}
    
    if card_one.isdigit():
        card_one = int(card_one)
    else:
        card_one = value[card_one]

    
    if card_two.isdigit():
        card_two = int(card_two)
    else:
        card_two = value[card_two]

    if 9 <= card_one + card_two <= 11:
        return True
    else:
        return False 
