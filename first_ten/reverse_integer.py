# Rev givern integer number

numbers = [101, 200, 501, -3456]


def solve(number):
    temp_num = str(number)
    sign = temp_num[0]
    result = temp_num[::-1]
    return "-" + result[:-1] if sign == '-' else result


[print(solve(n)) for n in numbers]
