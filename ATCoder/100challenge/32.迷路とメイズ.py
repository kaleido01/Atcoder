from collections import deque


while(True):
  w, h = map(int, input().split())
  if w==0 and h==0:
    break
  rightWall=[]
  bottomWall = []

  for i in range(h-1):
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    rightWall.append(x)
    bottomWall.append(y)
  x = list(map(int, input().split()))
  rightWall.append(x)

  maze = [ [[] for _ in range(w)]for _ in range(h)]

  for i in range(h):
    for j in range(w):
      if j != 0:
        if rightWall[i][j-1] == 0:
          maze[i][j].append(3)
      if j != w-1:
        if rightWall[i][j] == 0:
          maze[i][j].append(1)
      if i !=0:
        if bottomWall[i-1][j] == 0:
            maze[i][j].append(0)
      if i != h-1:
        if bottomWall[i][j] == 0:
          maze[i][j].append(2)


        
  que = deque()
  count = 1
  checked =[[False for _ in range(w)]for _ in range(h)]
  que.append([0,0,count])
  checked[0][0] = True


  dx = [0,1,0,-1]
  dy = [-1,0,1,0]

  isOK =False
  while (len(que) >.0):
    x,y,count = que.popleft()
    # print(x,y,count)
    for nextd in maze[y][x]:
      sx, sy = x,y
      sx += dx[nextd]
      sy += dy[nextd]
      if sx == w-1 and sy == h-1:
        print(count+1)
        isOK = True
        break
      # if not (0<= x < w) or not (0<= y < h):
      #   continue
      if checked[sy][sx] == True:
        continue
      checked[sy][sx] = True
      que.append([sx,sy,count+1])
    if isOK:
      break
  if not isOK:
    print(0)



