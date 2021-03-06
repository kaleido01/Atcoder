# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10**9)
INF=2 * 10**5
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input())for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from itertools import combinations, permutations, combinations_with_replacement
from collections import deque
import heapq



n, m, k= mapInt()

h = listInt()
c = listInt()

# que = []
# for i in range(n):
#   que.append((h[i],i))
  
# que.sort(reverse = True)

# print(que)

# for i in range(k):
#   c[i] -=1


nodes =[[] for i in range(n)]

for i in range(m):
  a, b = mapInt()
  a -= 1
  b -= 1
  
  if h[a] > h[b]:
    nodes[b].append(a)
  else:
    nodes[a].append(b)
    


# print(nodes)
dp = [INF for _ in range(n)]

# done = [[False for i in range(n)] for i in range(n)]

nextPos = []

# # 山の高さが小さい順に取り出していく
for i in range(n):
  heapq.heappush(nextPos,(h[i], i))


while(nextPos):
  # height , pos = que.pop(0)
  height , pos = heapq.heappop(nextPos)
  # print(que)
  
  if pos+1 in c:
    dp[pos] = 0
  for node in nodes[pos]:
    dp[node] = min(dp[pos]+1,dp[node])
    

for i in range(n):
  if dp[i] == INF:
    print(-1)
  else:
    print(dp[i])