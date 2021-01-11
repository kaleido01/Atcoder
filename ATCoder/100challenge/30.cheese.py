from collections import deque

h, w, n = map(int, input().split())

maze = [list(input()) for _ in range(h)]

que = deque()

for i in range(h):
  for j in range(w):
    if maze[i][j] == "S":

      que.append([j,i,0])
      
    
def bfs(count,target):
  while (len(que) >.0):
    x, y, count = que.popleft()

    if not (0<= x < w) or not (0<= y < h):
      continue
    if maze[y][x] == str(target):
      return [x,y,count]
    if maze[y][x] == "X":
      continue
    if checked[y][x] == True:
      continue
    checked[y][x] = True
    count +=1
    que.append([x+1,y,count])
    que.append([x-1,y,count])
    que.append([x,y+1,count])
    que.append([x,y-1,count])

count = 0
for i in range(1,n+1):
  checked = [[False for _ in range(w)] for _ in range(h)]
  s=bfs(count,i)
  x, y ,v = s
  que = deque()
  que.append([x,y,v])
  count = v
  
print(count)
