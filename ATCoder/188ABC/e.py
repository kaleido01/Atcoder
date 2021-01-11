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

n,m = mapInt()

a = listInt()

ans = [-1 * INF for i in range(n)]
done =[ False for i in range(n)]
nodes = [[] for i in range(n)]
for i in range(m):
  x, y = mapInt()
  x -=1
  y -=1
  nodes[x].append(y)
  


nq = []
for i in range(n):
  nq.append
q = deque()


for i in range(n):
  if not done[i]:
    done[i] = True
    minHeap = []
    heapq.heappush(minHeap,a[i])
    q.append([i,minHeap])

    while(q):
      # 先頭のキューを取り出す。取り出したキューは確定地点である。
      currentNode,costs = q.popleft()
      
      #自分が購入できる一番安い金
      # print("cost",cost)
      cost = costs[0]
      
      for node in nodes[currentNode]:
        done[node] = True
        w = a[node]
        if ans[node] < w - cost:
          ans[node] = w - cost
          
        heap = costs.copy()

        heapq.heappush(heap,w)

        q.append([node,heap])
          # heapq.heappush(minHeap, (ans[node], node))
    

ansss = -INF
# print(ans)
for v in ans:
  ansss = max(ansss,v)

print(ansss)