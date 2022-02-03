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
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from collections import deque
import heapq



n, m = mapInt()

minYear = []
kosuu = [0]  * (n+1)
for i in range(m):
  p,y = mapInt()
  # p -=1
  minYear.append((y,p,i))
  
minYear.sort()
ans =[]
def f(s):
  while(len(s)<6):
    s = "0" + s
  return s

for i in range(m):
  y, p,index = minYear[i]
  num = kosuu[p]
  
  s = f(str(p)) + f(str(num+1))
  ans.append((index,s))
  kosuu[p] += 1
  
ans.sort()

for v in ans:
  print(v[1])
  