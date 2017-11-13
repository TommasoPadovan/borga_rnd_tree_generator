import sys


def associated_permutation(pattern):
    k = len(pattern)
    out = [0]*k
    for i in range(1, k+1):
        min_ind = min_index(pattern)
        out[min_ind] = i
        pattern[min_ind] = sys.maxint
    return tuple(out)


def min_index(lst):
    m = sys.maxint
    min_ind = 0
    for i in range(0, len(lst)):
        if m > lst[i]:
            m = lst[i]
            min_ind = i
    return min_ind
