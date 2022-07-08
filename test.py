from typing import List
from num2words import num2words


def numToEng(n: int) -> str:
    q = "and"
    a = num2words(n)
    b = a.split()
    k = []

    for i in b:
        if i in q:
            continue
        k.append(i)
    m = " ".join(k)

    return m