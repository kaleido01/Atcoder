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
inithw = lambda h, w, v: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter

n, m = mapInt()

node = initDp(n)

for i in range(m):
  s,t = mapInt()
  s -= 1
  t -= 1
  node[s].append(t)
  
dp =init0(n)

for v in range(n-2, -1,-1):
  pas = len(node[v])
  now = 0
  for to in node[v]:
    now += dp[to]
  now /= pas
  now += 1
  dp[v] += now


# print(dp)


ans = dp[0]


for i in range(n):
  ansDp = init0(n)
  cutEdge = -1
  s = 0
  if len(node[i]) == 1:
    continue
  for j in node[i]:
    if dp[j] > s:
      cutEdge = j
      s = dp[j]

  for v in range(n-2, -1,-1):
    pas = len(node[v])
    if cutEdge in node[v] and v == i:
        pas -= 1
    now = 0
    for to in node[v]:
      if to == cutEdge and v == i:
          continue
      now += ansDp[to]
    now /= pas
    now += 1
    ansDp[v] = now
  # print(ansDp)
  ans = min(ans, ansDp[0])

print(ans)