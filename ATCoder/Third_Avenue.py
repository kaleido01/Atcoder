from collections import deque
h, w = map(int, input().split())

maze = [ list(input()) for _ in range(h)]
did = [ [False for _ in range(w)] for _ in range(h)]
warp =[[] for _ in range(50)]

que = deque()
for i in range(h):
  for j in range(w):
    if maze[i][j] == "S":

      que.appendleft([j,i,0])
      did[i][j] = True
    if ord("a") <= ord(maze[i][j]) <= ord("z"):
      warp[ord(maze[i][j]) - ord("a")].append([j,i])
      
      
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def f():
  while (len(que)>0):
    # print(que)
    x, y, count = que.popleft()
    for i in range(4):
      x2 = x+dx[i]
      y2 = y+dy[i]
      if not(0<= x2 < w) or not(0 <= y2 < h):
        continue
      if maze[y2][x2] == "#":
        continue
      if maze[y2][x2] == "G":
        return count+1
      if not did[y2][x2]:
        que.append([x2,y2,count+1])
        did[y2][x2] = True
      
    if ord("a") <= ord(maze[y][x]) <= ord("z"):
      t = ord(maze[y][x]) - ord("a")
      if len(warp[t]):
        for x2, y2 in warp[t]:
          # if len(v)==0:
          #   continue
          if not (x2 == x and y2 == y):
            que.append([x2,y2,count + 1])
            did[y2][x2] = True
        warp[t].clear()
  return -1

print(f())
