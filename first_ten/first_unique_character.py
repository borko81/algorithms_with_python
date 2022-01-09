# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.


def solution(sentense):
    words = {}

    for w in sentense:
        if w not in words:
            words[w] = 0
        words[w] += 1

    for pos, w in enumerate(sentense):
        if words[w] == 1:
            return f"First unique char: {w} found at positon {pos}"
    return -1


if __name__ == "__main__":
    print(solution("alphabet"))
    print(solution("barbados"))
    print(solution("crunchy"))
