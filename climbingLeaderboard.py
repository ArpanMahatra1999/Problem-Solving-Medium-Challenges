scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
scores = sorted(list(set(scores)))
index = 0
position = []
n = len(scores)
for i in alice:
    while n > index and i >= scores[index]:
        index += 1
    position.append(n + 1 - index)

print(position)