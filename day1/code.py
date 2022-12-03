def readFile():
    f = open('C:/AgodaGit/test/python/advent_of_code/day1/input.txt')
    return f.read()


def getElves(data):
    return data.split('\n\n')


def getCalories(elves):
    calories = []
    for e in elves:
        cals = e.split('\n')
        calories.append(sum([int(c) for c in cals]))
    return calories


def part1():
    data = readFile()
    elves = getElves(data)
    calories = getCalories(elves)
    return max(calories)


def part2():
    data = readFile()
    elves = getElves(data)
    calories = sorted(getCalories(elves), reverse=True)
    return sum(calories[:3])


print('part1', part1())
print('part2', part2())
