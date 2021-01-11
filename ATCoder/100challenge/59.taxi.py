import heapq
import math
from collections import deque

n, k = map(int, input().split())


fare = [0 for i in range(n)]
times = [0 for i in range(n)]

for i in range(n):
  x,y = map(int, input().split())
  fare[i] = x
  times[i] = y

nodes = [[] for _ in range(n)]

for i in range(k):
  s,t= map(int, input().split())
  s -= 1
  t -= 1
  nodes[s].append(t)
  nodes[t].append(s)
  

que = deque()
newNodes = [[] for _ in range(n)]

# done=[[False for _ in range(n)] for _ in range(n)]
# que.append((0,0, times[0]))
# # 頂点iからjへと辿れる新たな有向グラフを作成する
# while(len(que) > 0):
#   startPos, currentPos ,rest = que.popleft()
#   node = nodes[currentPos]
#   if currentPos == n-1:
#     continue
#   for nextDest in node:
#     #乗り継ぎして次の地点へ進む場合
#     if done[currentPos][nextDest] == False:
#       done[currentPos][nextDest] = True
#       newNodes[currentPos].append((nextDest))
#       que.append((currentPos,nextDest,times[currentPos]-1))
    
#     # 乗り継ぎせず次の地点へ進める場合
#     if rest>=1 and done[startPos][nextDest] == False:
#       done[startPos][nextDest] = True
#       newNodes[startPos].append(nextDest)
#       que.append((startPos,nextDest,rest-1))
# print(nodes)  
# print(newNodes)

# 頂点iからjへと辿れる新たな有向グラフを作成する
for i in range(n):
  done=[False for _ in range(n)]
  que.append((i, times[i]))
  done[i] = True
  while(len(que) > 0):
    pos ,rest = que.popleft()
    node = nodes[pos]
    if pos == n-1:
      continue
    
    for nextDest in node:
      # 乗り継ぎせず次の地点へ進める場合
      if rest>=1 and done[nextDest] == False:
        done[nextDest] = True
        newNodes[i].append(nextDest)
        que.append((nextDest,rest-1))

# print(newNodes)


ans = [math.inf for _ in range(n)]
ans[0] = 0
def dijkstra():
  minheap =[]
  
  heapq.heapify(minheap)
  heapq.heappush(minheap,(0,0))
  
  while(minheap):
    cost, pos = heapq.heappop(minheap)
    
    if cost > ans[pos]:
      continue
    
    for v in newNodes[pos]:
      if fare[pos] + cost < ans[v]:
        ans[v] = fare[pos] + cost
        heapq.heappush(minheap,(ans[v],v))


dijkstra()
print(ans[n-1])