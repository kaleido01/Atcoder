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


h, w, k = mapInt()

grid = inithw(h)


ans = h * w
for i in range(1 << (h-1)):
  line = 0
  result = 0
  for j in range(h-1):
    if (i >> j) & 1:
      line += 1
  a = [0 for i in range(line+1)]
  # print(line)
  result += line
  isCycle2 = False
  canAdd = True
  for j in range(w):
    lineIndex = 0
    b = a.copy()
    for p in range(h):
      # print(lineIndex, p, j)
      a[lineIndex] += ( 1 if grid[p][j] == "1" else 0)
      
      if (i >> p) & 1:
        lineIndex += 1
        
    isChecked = True
    for check in a:
      if check > k:
        # print("check",check)
        if not isCycle2:
          canAdd = False
          break
        result += 1
        # reset count
        isCycle2 =  False
        
        a = [a[i] - b[i] for i in range(line+1)]
        break
    if isChecked:
      isCycle2 = True
    else:
      isCycle2 = False
    if not canAdd:
      break
  if not canAdd:
    continue
  # print("result", result)
  # print("line", line)
  # print("a", a)
  ans = min(result, ans)
  
        
        
        
print(ans)