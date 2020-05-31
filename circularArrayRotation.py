a = [1, 2, 3]
k = 2
queries = [0, 1, 2]

j = len(a)

for x in range(k):
    n = a[j - 1]
    a.insert(0, n)
    print(a)
    a.pop(j)
    print(a)

newList = []

for m in queries:
    newList.append(a[m])

print(newList)
