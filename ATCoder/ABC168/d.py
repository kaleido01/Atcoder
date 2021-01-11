import heapq
import math

n,m = map(int, input().split())

nodes =[ []for i in range(n)]

for i in range(m):
  a, b = map(int, input().split())
  a -=1
  b -=1
  
  nodes[a].append(b)
  nodes[b].append(a)
  
  
# print(nodes)

costArray = [math.inf for _ in range(n)]
used = [False for _ in range(n)]
ansNum = [-1 for _ in range(n)]


def prim(start, nodes):
  minHeap = []
  heapq.heappush(minHeap,(0, start))
  
  while(minHeap):
    # 先頭のキューを取り出す。取り出したキューは確定地点である。
    # print(minHeap)
    # print(used)
    cost , currentNode = heapq.heappop(minHeap)
    
    # すでに加えられた頂点の場合はスキップ
    if used[currentNode]:
      continue
    # その頂点を全域木に加える
    used[currentNode] = True

    # その頂点から辿れるノード先のコストを計算して、最小値を更新する。
    for node in nodes[currentNode]:
      if costArray[node] > 1 + cost:
        costArray[node] = 1 + cost
        ansNum[node] = currentNode
      heapq.heappush(minHeap, (1 + cost, node))


prim(0,nodes)

# print("ansNum")
print("Yes")
for i in range(1, n):
  print(ansNum[i] + 1)

