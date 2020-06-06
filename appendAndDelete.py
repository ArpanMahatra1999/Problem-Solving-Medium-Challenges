s = list('abcd')
t = list('abcdert')
k = 10
m = len(s)
n = len(t)

for i in range(m):
    if s == t[0:len(s)]:
        break
    else:
        s.pop()
o = 2*len(s)
for j in range(m - i,n):
    s.append(t[j])
z = n - m + 2*i    
if (z <= k and (k - z)%2 == 0) or (z + o) <= k:
    print('Yes')
else:
    print('No')