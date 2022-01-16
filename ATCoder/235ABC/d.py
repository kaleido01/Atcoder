# -*- coding: utf-8 -*-
from pickle import TRUE
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h, w: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter

a, n = mapInt()

c = [False] * (10**6)

que = deque()
que.append([n, 0])
c[n] = True
ans = INF
while que:
  now, cnt = que.popleft()
  # print("now", now, cnt)
  if now == 1:
    ans = min(ans, cnt)
    # sys.exit()
  
  #操作A
  temp = now
  if (temp % a) == 0:
    before = temp // a
    if not c[before]:
      c[before] = True
      # print("a", before, cnt)
      que.append([before, cnt+1])

  #操作B
  temp = now
  if (temp <= 10): continue
  listTemp = list(str(temp))
  if listTemp[1] == "0": continue
  l = listTemp[0]
  newTemp = listTemp[1:]
  newTemp.append(l)
  before = int("".join(newTemp))
  if not c[before]:
    c[before] = True
    # print("tempB", before, cnt)
    que.append([before, cnt+1])
      
if ans == INF:
  print(-1)
else:
  print(ans)