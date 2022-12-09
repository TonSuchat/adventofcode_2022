def parseTrees(lines):
    trees = []
    for row in lines:
        arr = []
        for column in row:
            arr.append(int(column))
        trees.append(arr)
    return trees


def getMaxAdjacents(arr, row, col):
    return [max([currentRow[col] for currentRow in arr[:row]]), max(arr[row][:col]), max([currentRow[col] for currentRow in arr[row+1:]]), max(arr[row][col+1:])]


def getTreesScenicScore(arr, row, col):
    def getTotalTrees(curArr):
        total = 0
        for item in curArr:
            total += 1
            if item >= arr[row][col]:
                return total
        return total

    top = getTotalTrees([currentRow[col] for currentRow in arr[:row]][::-1])
    left = getTotalTrees(arr[row][:col][::-1])
    bottom = getTotalTrees([currentRow[col] for currentRow in arr[row+1:]])
    right = getTotalTrees(arr[row][col+1:])

    return top*left*bottom*right


lines = list(map(lambda x: x.strip("\n"), open(
    'input.txt', 'r').readlines()))
trees = parseTrees(lines)

totalVisible = len(trees[0])*2 + (len(trees)-2)*2
for r in range(1, len(trees)-1):
    for c in range(1, len(trees[r])-1):
        cur = trees[r][c]
        adjacent = getMaxAdjacents(trees, r, c)
        if any(x < cur for x in adjacent):
            totalVisible += 1

print('part1', totalVisible)

scenincScores = []
for r in range(1, len(trees)-1):
    for c in range(1, len(trees[r])-1):
        scenincScores.append(getTreesScenicScore(trees, r, c))
print('part2', max(scenincScores))
