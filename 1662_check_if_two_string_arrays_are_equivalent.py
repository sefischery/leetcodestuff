from typing import List


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    w1 = ''.join(word1)
    w2 = ''.join(word2)
    print(w1, w2)
    return True if w1 == w2 else False


word1 = ["ab", "c"]
word2 = ["a", "bc"]

print(arrayStringsAreEqual(word1, word2))