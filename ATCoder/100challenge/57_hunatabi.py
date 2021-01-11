import heapq
import math
n,k = map(int, input().split())

nodes = [[] for _ in range(n)]
weight = [[math.inf for _ in range (n)] for _ in range(n)]


def dijikstra(start, nodes,weight):
  minHeap = []
  heapq.heappush(minHeap,(0, start))
  while(minHeap):
    # 先頭のキューを取り出す。取り出したキューは確定地点である。
    cost , currentNode = heapq.heappop(minHeap)
    if cost > ans[currentNode]:
      continue
    
    for node in nodes[currentNode]:
      w = weight[currentNode][node]
      if ans[node] > w + cost:
        ans[node] = w + ans[currentNode]
        heapq.heappush(minHeap, (ans[node], node))
    


for _ in range(k):
  l = list(map(int, input().split()))
  if l[0] == 0:
    # 客からの依頼
    s = l[1]-1
    e = l[2]-1
    ans = [math.inf for _ in range(n)]
    ans[s] = 0
    dijikstra(s,nodes,weight)
    # print(ans)
    if ans[e] == math.inf:
      print(-1)
    else:
      print(ans[e])
  else:
    # 新しい運行
    s = l[1]-1
    e = l[2]-1
    nodes[s].append(e)
    nodes[e].append(s)
    if weight[s][e] >= l[3]:
      weight[s][e] = l[3]
      weight[e][s] = l[3]
    # print(nodes,weight)
  