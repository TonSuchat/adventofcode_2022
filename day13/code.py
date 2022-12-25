from collections import defaultdict
from functools import cmp_to_key

lines = list(map(lambda x: x.strip('\n'), open('input', 'r').readlines()))


def compare(left, right):
    if type(left) == type(right) is int:
        return left - right
    elif type(left) == type(right) is list:
        result = 0
        m, n = len(left), len(right)
        for i in range(min(m, n)):
            result = compare(left[i], right[i])
            if result:
                break
        if result == 0:
            if n < m:
                return float('inf')
            elif m == n:
                return 0
            return -float('inf')
        return result
    else:
        if type(left) is int:
            return compare([left], right)
        else:
            return compare(left, [right])


def solve():
    i = 1
    dict = defaultdict(list)
    key = False
    sum = 0
    for line in lines:
        if not line:
            continue
        dict[key] = eval(line)
        if key:
            if compare(dict[False], dict[True]) < 0:
                sum += i
            i += 1
        key = not key
    return sum


def solve2():
    dict = defaultdict(list)
    for i, line in enumerate(lines):
        if not line:
            continue
        dict[i] = eval(line)
    dict[i+1] = [[2]]
    dict[i+2] = [[6]]
    sortedDict = sorted(dict.values(), key=cmp_to_key(compare))
    i = sortedDict.index([[2]]) + 1
    j = sortedDict.index([[6]]) + 1
    return i*j


print('part1', solve())
print('part2', solve2())
