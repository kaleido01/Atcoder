# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
d4 = [(0,1), (1,0)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
intInput = lambda: int(input())
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

n = int(input())
grid = [ [] for _ in range(n)]

for i in range(n-1):
  a, b = mapInt()
  a -= 1
  b -= 1
  heapA = grid[b]
  heapq.heappush(heapA, a)
  
  heapB = grid[a]
  heapq.heappush(heapB, b)
  
  # grid[a].append(b)
  # if a > b:
  #   grid[b].append(a)
  # else:
  #   grid[a].append(b)
  
  

done = [False] * n

ans = []

def bfs(pos):
  # cur = [pos]
  ans.append(pos)
  
  nodes = grid[pos]
  while nodes:
    node = heapq.heappop(nodes)
    if done[node]: continue
    done[node] = True
    bfs(node)
    # cur.extend(road)
    ans .append(pos)
    # cur.append(pos)
  
  # return cur

done[0] = True
bfs(0)
  
for v in ans:
  print(v+1, end= " ")
  

