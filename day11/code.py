from itertools import groupby

lines = list(map(lambda x: x.strip('\n').strip(),
                 open('input', 'r').readlines()))
monkeys = [list(group)
           for key, group in groupby(lines, lambda x: x == '') if not key]


def getItems(line):
    return list(map(lambda x: int(x.strip()), line.split(':')[1].split(', ')))


def getOperation(line):
    return list(map(lambda x: int(x) if x.isdigit() else x, line.split(
        ':')[1].strip().replace('new = old', '').strip().split(' ')))


def getTest(line):
    return int(line.strip().split(':')[1].strip().split(' ')[2])


def getTestResult(lineTrue, lineFalse):
    return [int(lineFalse.split(':')[1].strip().split(' ')[3]), int(lineTrue.split(':')[1].strip().split(' ')[3])]


def evaluate(oldVal, newVal, operation):
    if operation == '+':
        return oldVal + newVal
    elif operation == '-':
        return oldVal - newVal
    elif operation == '*':
        return oldVal * newVal
    else:
        return oldVal // newVal

# items = [[79,98], [54, 65, 75, 74]]
# operations = [["*",19], ["+",6]]
# tests = [23, 19]
# testResults = [[3,2], [0,2]]
# inspects = [0, 0]


def process(round, isDivide=False):
    items = []
    operations = []
    tests = []
    testResults = []

    for monkey in monkeys:
        items.append(getItems(monkey[1]))
        operations.append(getOperation(monkey[2]))
        tests.append(getTest(monkey[3]))
        testResults.append(getTestResult(monkey[4], monkey[5]))

    inspects = [0] * len(monkeys)
    for _ in range(round):
        for i in range(len(items)):
            while items[i]:
                inspects[i] += 1
                item = items[i].pop(0)
                (operation, val) = operations[i]
                newVal = evaluate(item, val if isinstance(
                    val, int) else item, operation)
                if isDivide:
                    newVal //= 3
                else:
                    newVal %= 9699690
                throwToMonkey = testResults[i][newVal % tests[i] == 0]
                items[throwToMonkey].append(newVal)
    inspects.sort(reverse=True)
    return inspects[0]*inspects[1]


print('part1', process(20, True))
print('part2', process(10000))
