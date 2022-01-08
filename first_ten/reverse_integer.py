# Rev givern integer number

numbers = [101, 200, 501, -34567]


def solve(number):
    temp_num = str(number)
    sign = temp_num[0]
    result = temp_num[::-1]
    return "-" + result[:-1] if sign == '-' else result


def solve_two(number):
    sign = str(number)[0]
    result = ''

    if sign == '-':
        number = abs(number)

    while number:
        result += str(number % 10)
        number //= 10

    return "-" + result if sign == '-' else result


if __name__ == '__main__':
    [print(solve(n)) for n in numbers]
    [print(solve_two(n)) for n in numbers]
