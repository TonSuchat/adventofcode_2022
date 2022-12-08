import collections

cache = collections.defaultdict(int)

dirs = []
for line in map(lambda x: x.strip("\n"), open('input.txt', 'r').readlines()):
    if line.startswith('$'):
        cmd = line.split(' ')
        if cmd[1] == 'cd':
            if cmd[2] == '/':
                dirs.clear()
            elif cmd[2] == '..':
                dirs.pop()
            else:
                dirs.append(cmd[2])
    else:
        if not line.startswith('dir'):
            row = line.split(' ')
            for i in range(len(dirs)+1):
                cache["/".join(dirs[:i])] += int(row[0])

print('part1', sum(filter(lambda x: x < 100000, cache.values())))
print('part2', min(filter(lambda x: x >= (
    30000000 - (70000000 - cache[''])), cache.values())))
