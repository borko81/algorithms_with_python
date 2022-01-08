# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

import re
sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"


def solve(sentense):
    sentense = re.sub('[!.,]', '', sentense).split()

    return round(sum([len(w) for w in sentense]) / len(sentense), 2)


if __name__ == '__main__':
    print(solve(sentence1))
