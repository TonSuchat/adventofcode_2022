data = open('input.txt', 'r').readline()

arr1 = []
for i in range(len(data)):
    if data[i] in arr1:
        removeIndex = arr1.index(data[i])+1
        arr1 = arr1[removeIndex:]
    arr1.append(data[i])
    if len(arr1) >= 4:
        print('part1', i+1)
        break

arr2 = []
for i in range(len(data)):
    if data[i] in arr2:
        removeIndex = arr2.index(data[i])+1
        arr2 = arr2[removeIndex:]
    arr2.append(data[i])
    if len(arr2) >= 14:
        print('part2', i+1)
        break