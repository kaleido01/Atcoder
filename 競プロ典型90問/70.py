# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
init1 = lambda n: [-1 for _ in range(n)]

inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

# h, w = mapInt()
n = int(input())

m = []
xa = []
ya = []
# minX = INF
# maxX = -1 * INF
# minY = INF
# maxY = -1 * INF

for i in range(n):
  x, y = mapInt()
  # X, Y = x-y, x+y
  m.append((x, y))
  xa.append(x)
  ya.append(y)
  # minX = min(minX, X)
  # maxX = max(maxX, X)
  # minY = min(minY, Y)
  # maxY = max(maxY, Y)
  
# middleX = [INF, INF]
# middleY = [INF, INF]
# if (maxX + minX) % 2 == 0:
#   middleX[0] = (maxX + minX) // 2
# else:
#   middleX[0] = (maxX + minX) // 2
#   middleX[1] = (maxX + minX + 1) // 2
  
# if (maxY + minY) % 2 == 0:
#   middleY[0] = (maxY + minY) // 2
# else:
#   middleY[0] = (maxY + minY) // 2
#   middleY[1] = (maxY + minY + 1) // 2
  


middleX = statistics.median(xa)

middleY = statistics.median(ya)

ans = 0
# for v1 in middleX:
#   for v2 in middleY:
#     temp = 0
#     for i in range(n):
#       x, y = m[i]
#       temp += max(abs(x-v1), abs(y-v2))
#     ans = min(ans, temp)
  
  

for i in range(n):
  x, y = m[i]
  ans += abs(x-middleX) + abs(y-middleY)
print(int(ans))