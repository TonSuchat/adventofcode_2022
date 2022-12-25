import collections

grid = list(map(lambda x: x.strip('\n').strip(),
            open('input', 'r').readlines()))
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
nrow, ncol = len(grid), len(grid[0])


def getStartPoint():
    for row in range(nrow):
        for col in range(ncol):
            if grid[row][col] == 'S':
                return (row, col)


def getStartPoints():
    result = []
    for row in range(nrow):
        for col in range(ncol):
            if grid[row][col] == 'S' or grid[row][col] == 'a':
                result.append((row, col))
    return result


def getIndex(x, y):
    if grid[x][y] == "E":
        return 25  # to avoid getting this before 'z'
    return ord(grid[x][y]) - ord('a')


def solve(start):
    queue = collections.deque([(start, 0, 0)])
    visited = {start}

    while queue:
        (x, y), index, steps = queue.popleft()
        if grid[x][y] == 'E':
            return steps
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < nrow and 0 <= ny < ncol and (nx, ny) not in visited and getIndex(nx, ny) <= index+1:
                visited.add((nx, ny))
                queue.append(((nx, ny), getIndex(nx, ny), steps+1))

    return None


print('part1', solve(getStartPoint()))
print('part2', min(map(lambda x: solve(x) or float('inf'), getStartPoints())))
