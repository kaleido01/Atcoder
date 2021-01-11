from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

maze = [list(input()) for _ in range(r)]

que = deque()
que.append([sx-1,sy-1,0])
checked = [[False for _ in range(c)] for _ in range(r)]

def bfs(count =0):
  while (len(que) >.0):
    x, y, count = que.popleft()
    if x == gx-1 and y == gy-1:
      print(count)
      break
    if not (0<= x < c) or not (0<= y < r):
      continue
    if maze[y][x] == "#":
      continue
    if checked[y][x] == True:
      continue
    checked[y][x] = True
    count +=1
    que.append([x+1,y,count])
    que.append([x-1,y,count])
    que.append([x,y+1,count])
    que.append([x,y-1,count])
    
bfs()
