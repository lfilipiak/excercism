def proverb(*input_data: list, qualifier: str = None) -> list:

    answer = []

    for value, item in enumerate(input_data):
        if (input_data.index(item) == len(input_data) - 1) and len(input_data) >= 1:
            answer.append(
                f"And all for the want of a {qualifier if qualifier != None else ''} {input_data[0]}.".replace(
                    "  ", " "
                )
            )
            return answer
        answer.append(f"For want of a {item} the {input_data[value + 1]} was lost.")

    return answer


input_data = ["nail"]
print(proverb(*input_data, qualifier=None))
