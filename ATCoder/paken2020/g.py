# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter


n, m= mapInt()

l = [0] * m
r = [0] * m
x = [0] * m

for i in range(m):
  s,t,u = mapInt()
  # print(p,q,r)
  # p -= 1
  # q -= 1
  l[i] = s
  r[i] = t
  x[i] = u
  
ans = -1
for i in range(1<<n):
  sn = [0] * (n+1)

  for j in range(n):
    if (i >> j) & 1 == 1:
      sn[j+1] = sn[j] + 1
    else:
      sn[j+1] = sn[j]
  
  uso = False
  # print(sn)
  for j in range(m):
    # print(sn[r[j]], sn[l[j]-1])
    if sn[r[j]] - sn[l[j]-1] != x[j]:
      uso = True
      break
  
  if not uso:
    # print(sn)
    ans = max(ans, sn[n])
    
    

print(ans)