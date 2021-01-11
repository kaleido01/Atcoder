from itertools import permutations
import math
n = int(input())

x = [0] * n
y=  [0] * n
for i in range(n):
  p,q = map(int, input().split())
  x[i] = p
  y[i] = q
  


patern = [i for i in range(n)]

allp = list(permutations(patern, n))
l = len(allp)
ans = 0


for p in allp:

  for i in range(len(p)-1):
    z = (x[p[i]] - x[p[i+1]]) ** 2 + (y[p[i]] - y[p[i+1]]) **2
    ans  += math.sqrt(z)
      


print(ans/l)
    