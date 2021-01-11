import heapq
import math

v,e,k = map(int, input().split())

nodes = [[] for _ in range(v)] 

used = [False for _ in range(v)]
maxCost=[]
for i in range(e):
  s,t,d = map(int, input().split())
  s -= 1
  t -= 1
  nodes[s].append((t,d))
  nodes[t].append((s,d))

# print(weight,nodes)
def prim(start, nodes):
  minHeap = []
  heapq.heappush(minHeap,(0, start))
  
  res= 0
  while(minHeap):
    # 先頭のキューを取り出す。取り出したキューは確定地点である。
    # print(minHeap)
    # print(used)
    cost , currentNode = heapq.heappop(minHeap)
    
    # すでに加えられた頂点の場合はスキップ
    if used[currentNode]:
      continue
    # その頂点を全域木に加え、コストを加える
    used[currentNode] = True
    res += cost
    maxCost.append(cost)
    
    
    # その頂点から辿れるノード先のコストを計算して、最小値を更新する。
    for node in nodes[currentNode]:
      node, weight = node
      heapq.heappush(minHeap, (weight, node))
    
  return res
    

res = prim(0,nodes)
maxCost.sort(reverse=True)
for i in range(k-1):
  res -= maxCost[i]
print(res)