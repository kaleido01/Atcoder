from collections import deque

n = int(input())


tree = [[] for _ in range(n+1)]

for i in range(n):
  x = list(map(int,input().split()))
  for v in x[2:]:
    tree[x[0]].append(v)


que = deque()
que.append([1,0])
ans = [10001] * (n+1)
checked = [False] * (n+1)

def bfs(count =0):
  while (len(que) >.0):
    num,count = que.popleft()
    if checked[num] == True:
      continue
    checked[num] = True
    ans[num] = min(ans[num], count)
    count +=1
    if len(tree[num])>0:
      for v in tree[num]:
        que.append([v,count])
    
bfs()

for i in range(1, len(ans)):
  if ans[i] ==10001:
    print(i,-1)
  else:
    print(i, ans[i])
  