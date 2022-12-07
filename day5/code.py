lines = list(map(lambda x: x.strip("\n"), open('input.txt', 'r').readlines()))
stackLines, moves = lines[:lines.index("") - 1], list(
    map(lambda split: (int(split[1]), int(split[3]) - 1, int(split[5]) - 1),
        map(lambda x: x.split(" "), lines[lines.index("") + 1:])))


def parseStacks(stacksLines):
    columns = len(stacksLines[0]) // 4 + 1
    stacks = [[] for _ in range(columns)]

    for l in stacksLines:
        for i in range(0, columns):
            char = l[i * 4 + 1]
            if char != " ":
                stacks[i].append(char)
    return stacks


stacks = parseStacks(stackLines)
for count, fromRow, toRow in moves:
    toMove = stacks[fromRow][:count]
    stacks[fromRow], stacks[toRow] = stacks[fromRow][count:], toMove[::-1] + stacks[toRow]
print("part1", "".join(map(lambda x: x[0], stacks)))

stacks = parseStacks(stackLines)
for count, fromRow, toRow in moves:
    toMove = stacks[fromRow][:count]
    stacks[fromRow], stacks[toRow] = stacks[fromRow][count:], toMove + stacks[toRow]
print("part2", "".join(map(lambda x: x[0], stacks)))
