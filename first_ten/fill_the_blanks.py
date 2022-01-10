# Given an array containing None values fill in the None values with most recent
# non None value in the array
array1 = [1, None, 2, 3, None, None, 5, None]


def solution(array: list):
    new_arr = []
    not_null = 0
    for n in array:
        if n is not None:
            new_arr.append(n)
            not_null = n
        else:
            new_arr.append(not_null)
    return new_arr


if __name__ == "__main__":
    print(solution(array1))
