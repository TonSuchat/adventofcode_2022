dirs = {'U': (1, 0), 'R': (0, 1), 'D': (-1, 0), 'L': (0, -1)}


def solve(ropeLen):
    visited = {(0, 0)}
    ropes = [(0, 0)] * ropeLen
    for move, steps in list(map(lambda x: x.split(' '), open('input', 'r').readlines())):
        for _ in range(int(steps)):
            ropes[-1] = (ropes[-1][0] + dirs[move][0],
                         ropes[-1][1] + dirs[move][1])
            for i in range(len(ropes)-2, -1, -1):
                curY, curX = ropes[i][0], ropes[i][1]
                nextY, nextX = ropes[i+1][0], ropes[i+1][1]
                diffY, diffX = nextY-curY, nextX-curX
                if abs(diffY) > 1 or abs(diffX) > 1:
                    ropes[i] = (
                        ropes[i][0] + (diffY if abs(diffY) == 1 else diffY//2),
                        ropes[i][1] + (diffX if abs(diffX) == 1 else diffX//2)
                    )
            visited.add(ropes[0])
    return len(visited)


print('part1', solve(2))
print('part2', solve(10))
