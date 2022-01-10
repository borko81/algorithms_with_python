# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common.

sentence1 = "We are really pleased to meet you in our city"
sentence2 = "The city was hit by a really heavy storm"


def solution(sen1, sen2):
    sen1 = set(sen1.split())
    sen2 = set(sen2.split())

    different = sen1 ^ sen2
    same = sen1 & sen2

    return sorted(different), sorted(same)


if __name__ == "__main__":
    print(solution(sentence1, sentence2))
