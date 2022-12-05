CONTAINS = 'contains'
OVERLAP = 'overlap'


def readFile():
    f = open('input.txt')
    return f.read()


def getItems(data):
    return data.split('\n')


def parse(data):
    (first, second) = data.split('-')
    return (int(first), int(second))


def contains(l1, l2, r1, r2):
    return (l1 <= r1 and l2 >= r2) or (l1 >= r1 and l2 <= r2)


def overlap(l1, l2, r1, r2):
    return min(l2, r2) - max(l1, r1) >= 0


def getTotal(items, type):
    total = 0
    for item in items:
        (l, r) = item.split(',')
        (l1, l2) = parse(l)
        (r1, r2) = parse(r)
        if type is CONTAINS:
            if contains(l1, l2, r1, r2):
                total += 1
        elif type is OVERLAP:
            if overlap(l1, l2, r1, r2):
                total += 1
    return total


def part1():
    data = readFile()
    items = getItems(data)
    return getTotal(items, CONTAINS)


def part2():
    data = readFile()
    items = getItems(data)
    return getTotal(items, OVERLAP)


print('part1', part1())
print('part2', part2())
