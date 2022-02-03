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


n = int(input())


grid = [ [] for i in range(n)]
for i in range(n-1):
    u, v, w = mapInt()
    u -= 1
    v -= 1
    grid[u].append((v, w))
    grid[v].append((u, w))


ans = [-1] * n
ans[0] = 0

def isEven(x):
    return x % 2 == 0

def dfs(pos, even):
    edges = grid[pos]
    for edge in edges:
        # print(pos, edge)
        npos, w = edge
        if ans[npos] == -1:
            
            # 両方偶数 or 奇数の場合は直前と同じ色を塗る
            if (even and isEven(w)):
                ans[npos] = ans[pos]
                dfs(npos, True)
            elif (not even and not isEven(w)):
                ans[npos] = 1- ans[pos]
                dfs(npos, True)
            elif even and not isEven(w):
                ans[npos] = 1 - ans[pos]
                dfs(npos, False)
            else:
                ans[npos] = ans[pos]
                dfs(npos, False)
    
dfs(0, True)

print(*ans)