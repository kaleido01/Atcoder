from collections import deque
import heapq
import math
n,m,k,s = map(int, input().split())
p,q = map(int, input().split())

# 0はsafe 1はdanger 2はout
dangerLevel =[0] *n
out = []



for i in range(k):
  index = int(input())
  index -= 1
  out.append(index)
  dangerLevel[index] = 2
  

nodes =[[] for i in range(n)]
for i in range(m):
  start, end = map(int, input().split())
  start -=1
  end -=1
  nodes[start].append(end)
  nodes[end].append(start)
  
# 幅優先でゾンビの町からS進んだところを危険な町として登録
def bfs(que,nodes):
  while(len(que) >0):
    pos, count = que.popleft()
    for nextPos in nodes[pos]:
      if seen[nextPos]:
        continue
      if dangerLevel[nextPos] ==2:
        continue
      # if nextPos == 0 or nextPos == n-1:
      #   continue
      seen[nextPos] = True
      dangerLevel[nextPos] = 1
      if count -1 == 0:
        continue
      else:
        que.append((nextPos,count-1))
    

que = deque()
for i in out:
  seen =[False] * n
  que.append((i, s))
  seen[index] = True
  bfs(que,nodes)



  
# ダイクストラ法で最小金額を計算
ans = [3*10**10 for _ in range(n)]

def dijikstra(start, nodes):
  minHeap = []
  heapq.heappush(minHeap,(0, start))
  while(minHeap):
    # 先頭のキューを取り出す。取り出したキューは確定地点である。
    cost , currentNode = heapq.heappop(minHeap)

    if cost > ans[currentNode]:
      continue
    
    for node in nodes[currentNode]:
      if dangerLevel[node] == 2:
        continue
      w = 0
      if node == n-1:
        w = 0
      elif dangerLevel[node] ==0:
        w = p
      else:
        w = q
      if ans[node] > w + cost:
        ans[node] = w + ans[currentNode]
        heapq.heappush(minHeap, (ans[node], node))
ans[0] = 0
dijikstra(0,nodes)
# print(dangerLevel)
# print(nodes)
# print(ans)
print(ans[n-1])
