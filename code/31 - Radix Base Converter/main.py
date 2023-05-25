def convert(number: int, base: int):
    number = str(number)[::-1]
    result = 0
    for key, digit in enumerate(number):
        result += int(digit) * (base**key)

    return result
