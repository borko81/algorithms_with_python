# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

n = 35


def solution(n):
    prime_numers = []
    for num in range(2, n):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            prime_numers.append(num)
    return prime_numers


if __name__ == "__main__":
    print(solution(n))
