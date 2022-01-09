# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4]
B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
C = [1, 1, 2, 3, 7]


def solution(arr):
    mass = range(len(arr) - 1)

    bigger = all(arr[i] >= arr[i + 1] for i in mass)
    smaller = all(arr[i] <= arr[i + 1] for i in mass)

    return bigger or smaller


if __name__ == "__main__":
    print(solution(A))
    print(solution(B))
    print(solution(C))
