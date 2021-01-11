import sys
# def input():
#     return sys.stdin.readline()[:-1]
from collections import deque
sys.setrecursionlimit(10**8) #再帰関数の呼び出し制限
n, q = map(int, input().split())

tree=[[]  for _ in range(n+1)]
for i in range(n-1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

ans =[0] * (n+1)
didCheck = [False] * (n+1)

for i in range(q):
  s, t = map(int, input().split())
  ans[s] += t

stack = deque()

# def dfs(start,p = 0):
#   ans[start] += ans[p]
#   stack.appendleft
#   for i in range(start+1, n+1):
#     if tree[start][i] == 0:
#       continue
#     dfs(i,start)

def dfs():
  while(len(stack)>0):
    position,parent = stack.pop()
    ans[position] += ans[parent]
    for v in (tree[position]):
      
      # 親でないことを確認する。
      if  v == parent:
        continue
      stack.appendleft([v,position])
      
stack.appendleft([1,0])

dfs()

for i in range(1,len(ans)):
  if i != 0:
    print(ans[i])