# -*- coding: utf-8 -*-
from socket import inet_aton
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
from operator import itemgetter, truediv
from collections import defaultdict

h, w = mapInt()

grid = [list(input()) for _ in range(h)]
# print(grid)

a1 = []
a2 = []
a3 = []
a4 = []
for i in range(h):
    left = 0
    x = [0] * (w)
    for j in range(w):
        if grid[i][j] == "#":
            left = j+1
        else:
            x[j] = j-left+1
    a1.append(x)
    
    right = w-1
    y = [0] * w
    for j in range(w-1, -1, -1):
        if grid[i][j] == "#":
            right = j-1
        else:
            y[j] = right - j + 1
    a2.append(y)
for i in range(w):
    left = 0
    x = [0] * (h)
    for j in range(h):
        if grid[j][i] == "#":
            left = j+1
        else:
            x[j] = j-left+1
    a3.append(x)
    
    right = h-1
    y = [0] * h
    for j in range(h-1, -1, -1):
        if grid[j][i] == "#":
            right = j-1
        else:
            y[j] = right - j + 1
    a4.append(y)

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, a1[i][j]+ a2[i][j] + a3[j][i] + a4[j][i] - 3)

print(a1[1], a2[1], a3[1], a4[1])
print(ans)