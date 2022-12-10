dirs = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0), }


def solve(ropeLen):
    visited = {(0, 0)}
    rope = [(0, 0)] * ropeLen
    for move, steps in list(map(lambda x: x.strip("\n").split(" "), open('input', 'r').readlines())):
        for _ in range(int(steps)):
            rope[-1] = (rope[-1][0] + dirs[move][0],
                        rope[-1][1] + dirs[move][1])
            for i in range(len(rope) - 2, -1, -1):
                if abs(rope[i + 1][0] - rope[i][0]) > 1 or abs(rope[i + 1][1] - rope[i][1]) > 1:
                    diffY = rope[i + 1][0] - rope[i][0]
                    diffX = rope[i + 1][1] - rope[i][1]

                    rope[i] = (
                        rope[i][0] + (diffY if abs(diffY)
                                      == 1 else diffY // 2),
                        rope[i][1] + (diffX if abs(diffX) == 1 else diffX // 2)
                    )
            visited.add(rope[0])
    return len(visited)


print(solve(2))
print(solve(10))
