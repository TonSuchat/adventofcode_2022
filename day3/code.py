from collections import Counter


def readFile():
    f = open('C:/AgodaGit/test/python/advent_of_code/day3/input.txt')
    return f.read()


def getItems(data):
    return data.split("\n")


def getCompartments(item):
    mid = len(item)//2
    return (item[:mid], item[mid:])


def getPriority(intersections):
    total = 0
    for i in intersections:
        if i.isupper():
            total += ord(i)-38
        else:
            total += ord(i)-96
    return total


def part1():
    data = readFile()
    items = getItems(data)
    total = 0
    for item in items:
        (compartment1, compartment2) = getCompartments(item)
        set1, set2 = set(compartment1), set(compartment2)
        intersections = list(set1 & set2)
        total += getPriority(intersections)
    return total


def part2():
    data = readFile()
    items = getItems(data)
    groups = [items[n:n+3] for n in range(0, len(items), 3)]
    total = 0
    for group in groups:
        set1, set2, set3 = set(group[0]), set(group[1]), set(group[2])
        intersections = list(set1 & set2 & set3)
        total += getPriority(intersections)
    return total


print('part1', part1())
print('part2', part2())
