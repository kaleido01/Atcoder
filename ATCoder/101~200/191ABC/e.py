# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
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
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n, m = mapInt()


nodes = [[] for _ in range(n)]
weight = [[0 for _ in range (n)] for _ in range(n)]

for i in range(m):
  a, b, c = mapInt()
  a -= 1
  b -=1
  weight[a][b] = c
  nodes[a].append(b)


def dijikstra(start, nodes,weight):
  minHeap = []
  heapq.heappush(minHeap,(0, i))
  while(minHeap):
    # 先頭のキューを取り出す。取り出したキューは確定地点である。
    cost , currentNode = heapq.heappop(minHeap)
    # done[currentNode] = True
    if cost > ans[currentNode]:
      continue
    
    for node in nodes[currentNode]:
      w = weight[currentNode][node]
      if ans[node] > w + cost:
        ans[node] = w + ans[currentNode]
        heapq.heappush(minHeap, (ans[node], node))
    


for i in range(n):
    done = [ False for _ in range(n)]
    ans = [math.inf for _ in range(n)]
    dijikstra(i,nodes,weight)
    ans[i] = 0
    print(ans)
    if ans[i] == math.inf:
      print(-1)
    else:
      print(ans[i])
