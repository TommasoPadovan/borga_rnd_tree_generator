import random


def tryAndFix(n):
    seq = ['(', ')'] * n
    random.shuffle(seq)

    stack = []
    result = []

    balance = 0
    prev = 0
    for pos in range(len(seq)):
        balance += 1 if seq[pos] == '(' else -1
        if balance == 0:
            if seq[prev] == '(':
                result.extend(seq[prev: pos + 1])
            else:
                result.append('(')
                stack.append([')' if v == '(' else '(' for v in seq[prev + 1: pos]])
            prev = pos + 1

    for lst in reversed(stack):
        result.append(')')
        result.extend(lst)

    return result


# dic = {}
#
# for i in range(1, 10000000):
#     p = ''.join(tryAndFix(3))
#     if p in dic:
#         dic[p] += 1
#     else:
#         dic[p] = 1
#
# for key in dic:
#     print dic[key]
