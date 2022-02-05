# -*- coding: utf-8 -*-
from collections import deque
import sys
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

m = int(input())

grid =[ [] for i in range(9)]

for i in range(m):
  u, v = mapInt()
  u, v = u-1, v-1
  grid[u].append(v)
  grid[v].append(u)

# print(grid)

cur = listInt()

s = 0
for i in range(8):
  cur[i] -= 1
  s += cur[i]
empty = 36 - s
# print(empty)
g = []
for i in range(8):
  g.append(i)
  


que = deque()

done= {}
que.append((cur, empty, 0))


def isDone(cur):
  num = 0
  for i in range(8):
    num += cur[i] * (10 ** i)
    
  if num in done:
    return True
  else:
    done[num] = True
    return False

while que:
  cur, empty, ans = que.popleft()
  isClear = True
  # print(cur, empty)
  for i in range(8):
    if cur[i] != g[i]:
      isClear = False
  if isClear:
    print(ans)
    sys.exit()
  
  for i in range(8):
    nextNodes = grid[cur[i]]
    # print(nextNodes)
    for v in nextNodes:
      if v == empty:
        na = cur.copy()
        na[i] = empty
        if isDone(na): continue
        nempty = cur[i]
        
        que.append((na, nempty, ans+1))


print("-1")
  
  
