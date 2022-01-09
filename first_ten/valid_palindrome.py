# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

s = 'radkar'


def solution(s):
    for i in range(len(s)):
        temp = s[:i] + s[i + 1:]
        if temp == temp[::-1]:
            return True, temp
    return s == s[::-1]


if __name__ == '__main__':
    print(solution(s))
