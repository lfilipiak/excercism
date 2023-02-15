def prime(number):

    candidate = 3
    prime_number = 0
    count = 1

    if number == 1 and type(number) is int:
        return 2

    if number < 1 or type(number) is not int:
        raise ValueError("there is no zeroth prime")

    while count <= number - 1:
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                candidate += 1
                break
        else:
            prime_number = candidate
            candidate += 1
            count += 1

    return prime_number
