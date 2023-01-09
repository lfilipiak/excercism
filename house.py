def recite(start_verse, end_verse):

    BEGIN = "This is the "
    answer = []

    verb = [
        "house that Jack built.",
        "malt that lay in",
        "rat that ate",
        "cat that killed",
        "dog that worried",
        "cow with the crumpled horn that tossed",
        "maiden all forlorn that milked",
        "man all tattered and torn that kissed",
        "priest all shaven and shorn that married",
        "rooster that crowed in the morn that woke",
        "farmer sowing his corn that kept",
        "horse and the hound and the horn that belonged to",
    ]

    for how_many in range(end_verse - start_verse + 1):
        answer.append(BEGIN + " the ".join(verb[how_many + start_verse - 1 :: -1]))

    return answer


print(recite(4, 8))
