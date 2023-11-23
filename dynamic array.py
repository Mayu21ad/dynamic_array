import math
import os
import random
import re
import sys

def dynamicArray(n, queries):
    seq = [[] for _ in range(n)]
    lastanswer = 0
    result = []

    for q, x, y in queries:
        if q == 1:
            idx = (x ^ lastanswer) % n
            seq[idx].append(y)
        else:
            idx = (x ^ lastanswer) % n
            v = y % len(seq[idx])
            lastanswer = seq[idx][v]
            result.append(lastanswer)

    return result


