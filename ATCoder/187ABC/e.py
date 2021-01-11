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
from collections import deque



n = int(input())

A = [ 0 for i in range(n)]
B = [ 0 for i in range(n)]

nodes = [ [] for i in range(n)]


for i in range(n-1):
  a, b = mapInt()
  a -= 1
  b -= 1
  # edge.append([a,b])
  A[i] = a
  B[i] = b
  nodes[a].append(b)
  nodes[b].append(a)
  
  
depth = [-1 for i in range(n)]
# depth[0] = 0
def depthDFS(a, d):
  depth[a] = d
  for node in nodes[a]:
    if depth[node] == -1:
      depthDFS(node, d+1)
    
depthDFS(0,0)

    
# q = [0]
# while q:
#     at = q.pop()
#     for node in nodes[at]:
#         if depth[node] == -1:
#             depth[node] = depth[at] + 1
#             q.append(node)
    

Q = int(input())

dp = [0 for i in range(n)]
for i in range(Q):
  t, e, x = mapInt()
  e -=1
  
  # vaが通る頂点vbが通らない頂点
  va, vb = (A[e], B[e]) if t == 1 else (B[e], A[e])
  
  if depth[va] > depth[vb]:
    dp[va] += x
  else:
    dp[0] += x
    dp[vb] -= x
    


done = [False for i in range(n)]

que = deque()

que.append(0)
done[0] = True

while(len(que) > 0):
  currentNode = que.popleft()
  
  for node in nodes[currentNode]:
    if done[node]:continue
    done[node] = True
    dp[node] += dp[currentNode]
    que.append(node)
    

  
for ans in dp:
  print(ans)