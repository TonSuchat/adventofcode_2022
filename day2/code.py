def readFile():
    f = open('C:/AgodaGit/test/python/advent_of_code/day2/input.txt')
    return f.read()


dict_score = {'X': 1, 'Y': 2, 'Z': 3}
dict_matchup = {'X': 'C', 'Y': 'A', 'Z': 'B', 'C': 'X', 'A': 'Y', 'B': 'Z'}
dict_lost_matchup = {'A': 'Z', 'B': 'X', 'C': 'Y'}
dict_draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
dict_result = {'X': 'L', 'Y': 'D', 'Z': 'W'}


def getScoreWithMatchUp(data):
    (opponent, you) = data.split(" ")
    # check if draw
    if dict_draw[opponent] == you:
        return 3 + dict_score[you]
    # is you win?
    if dict_matchup[you] == opponent:
        return 6 + dict_score[you]
    else:
        return dict_score[you]


def getScoreWithResult(data):
    (opponent, end) = data.split(" ")
    result = dict_result[end]
    if result == 'W':
        return 6 + dict_score[dict_matchup[opponent]]
    elif result == 'D':
        return 3 + dict_score[dict_draw[opponent]]
    else:
        return dict_score[dict_lost_matchup[opponent]]


def part1():
    data = readFile()
    rounds = data.split('\n')
    total = 0
    for round in rounds:
        total += getScoreWithMatchUp(round)
    return total


def part2():
    data = readFile()
    rounds = data.split('\n')
    total = 0
    for round in rounds:
        total += getScoreWithResult(round)
    return total


print('part1', part1())
print('part2', part2())
