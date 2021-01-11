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


n, m = mapInt()

h = listInt()

nodes = [ [] for i in range(n)]
for i in range(m):
  a, b = mapInt()
  a -= 1
  b -= 1
  
  if h[a] > h[b]:
    nodes[b].append(a)
  elif h[a] < h[b]:
    nodes[a].append(b)
  else:
    nodes[a].append(b)
    nodes[b].append(a)
    
    
ans = [False] * n

for i in range(n):
  if len(nodes[i]) == 0:
    ans[i] = True

count = 0

for boo in ans:
  if boo:
    count +=1
    
print(count)
