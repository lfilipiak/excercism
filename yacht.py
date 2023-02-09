# Score categories.
# Change the values as you see fits

YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"


class Poker:
    def __init__(self) -> None:
        self.single_points = 0
        self.cat = ""

    def set_score(self, score):
        self.score = score

    def yacht(self):
        return 50 if len(set(self.score)) == 1 else 0

    def singles(self, cat: str):
        category = {
            "ones": 1,
            "twos": 2,
            "threes": 3,
            "fours": 4,
            "fives": 5,
            "sixes": 6,
        }

        for i in self.score[::-1]:
            if i != int(category[cat]):
                self.score.remove(i)
        return sum(self.score)

    def full(self):
        if len(set(self.score)) == 2 and (
            self.score.count(self.score[0]) == 2
            or self.score.count(self.score[0]) == 3  # noqa
        ):
            return sum(self.score)
        return 0

    def four_of_a_kind(self):
        if self.score.count(self.score[0]) >= 4:
            return self.score[0] * 4
        elif self.score.count(self.score[1]) == 4:
            return self.score[1] * 4
        return 0

    def little_straight(self):
        return 30 if {1, 2, 3, 4, 5} == set(self.score) else 0

    def big_straight(self):
        return 30 if {2, 3, 4, 5, 6} == set(self.score) else 0

    def choice(self):
        return sum(self.score)


abc = Poker()


def score(args: list, method: str) -> int:

    abc.set_score(args)

    if method == YACHT:
        return abc.yacht()

    if method == ONES:
        return abc.singles("ones")

    if method == TWOS:
        return abc.singles("twos")

    if method == THREES:
        return abc.singles("threes")

    if method == FOURS:
        return abc.singles("fours")

    if method == FIVES:
        return abc.singles("fives")

    if method == SIXES:
        return abc.singles("sixes")

    if method == FULL_HOUSE:
        return abc.full()

    if method == FOUR_OF_A_KIND:
        return abc.four_of_a_kind()

    if method == LITTLE_STRAIGHT:
        return abc.little_straight()

    if method == BIG_STRAIGHT:
        return abc.big_straight()

    if method == CHOICE:
        return abc.choice()
