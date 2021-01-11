import heapq
import math

v,e,r = map(int, input().split())

nodes = [[] for _ in range(v)] 
# weight = [[ 0 for _ in range(v)] for _ in range(v)]
ans = [math.inf for _ in range(v)]

ans[r] = 0
for i in range(e):
  s,t,d = map(int, input().split())
  nodes[s].append((t,d))
  # weight[s][t] = d

# print(weight,nodes)
def dijkstra(start, nodes):
  minHeap = []
  heapq.heappush(minHeap,(0, start))
  
  while(minHeap):
    # 先頭のキューを取り出す。取り出したキューは確定地点である。
    cost , currentNode = heapq.heappop(minHeap)
    
    # すでにコストが現在の最小を上回っている場合はスキップ
    if cost > ans[currentNode]:
      continue
    
    # その頂点から辿れるノード先のコストを計算して、最小値を更新する。
    for node in nodes[currentNode]:
      node, weight = node
      if ans[node] > weight + cost:
        ans[node] = weight + ans[currentNode]
        heapq.heappush(minHeap, (ans[node], node))
    


dijkstra(r,nodes)

for v in ans:
  if v == math.inf:
    print("INF")
  else:
    print(v)