import collections

input = list(map(lambda x: x.strip("\n").split(
    " "), open('input', 'r').readlines()))
cache, queue, x, i, counter = {}, collections.deque(), 1, 0, 0
while queue or i < len(input):
    if i < len(input):
        queue.append(
            (counter + 2, int(input[i][-1])) if len(input[i]) == 2 else (counter + 1, 0))
        counter += len(input[i])
    if i == queue[0][0]:
        x += queue.popleft()[1]
    cache[i + 1], i = x, i + 1

print(sum(map(lambda x: cache[x] * x, range(20, 221, 40))))

crt = ""
for i in range(1, 241):
    cycle, val = (i-1) % 40, cache[i]
    if cycle == 0:
        crt += "\n"
    crt += "#" if val-1 <= cycle <= val+1 else "."
print(crt)
# FJUBULRZ
