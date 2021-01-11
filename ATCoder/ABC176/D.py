import sys
import math 
from collections import deque

h,w = map(int, input().split())
ch,cw = map(int, input().split())
dh,dw = map(int, input().split())

maze = [ list(input())for _ in range(h)]
done =  [ [False for _ in range(w)] for _ in range(h)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

que1 = deque()
que2 = deque()
done[ch-1][cw-1] = True
que1.append((cw-1, ch-1))
# que2.append((cw-1, ch-1))
cost = 0
while(True):
  if len(que1) == 0:
    break
  while(len(que1)>0):
    x, y = que1.popleft()
    for i in range(4):
      sx ,sy = x,y
      sx += dx[i]
      sy += dy[i]
      if not (0<= sx < w) or not (0<= sy < h):
        continue
      if sx == dw -1 and sy == dh -1:
        print(cost)
        sys.exit()
      if maze[sy][sx] == "#":
        continue
      if done[sy][sx]:
        continue
      done[sy][sx] = True
      que1.append((sx,sy))
    que2.append((x,y))
    
  while(len(que2)>0):
    x, y = que2.popleft()
    for i in range(-2, 3):
      for j in range(-2,3):
        # if -1 <= i <=1 and -1<= j <= 1:
        #   continue
        sx ,sy = x,y
        sx += j
        sy += i
        if not (0<= sx < w) or not (0<= sy < h):
          continue
        if sx == dw -1 and sy == dh -1:
          print(cost+1)
          sys.exit()
        if maze[sy][sx] == "#":
          continue
        if done[sy][sx]:
          continue
        done[sy][sx] = True
        que1.append((sx,sy))
  # print(que1)
  cost += 1


print(-1)
