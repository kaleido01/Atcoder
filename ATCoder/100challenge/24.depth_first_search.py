import sys
from collections import deque
# sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限
h, w = map(int, input().split())
 
c =[]
for i in range(h):
  c.append([v for v in list(input())])

sx,sy= 0,0
for i in range(h):
  for j in range (w):
    if c[i][j] == "s":
      sy, sx = i,j

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# def dfs(x,y):
#   c[y][x] = "#"
#   for i in range(4):
#     nextx = x + dx[i]
#     nexty = y + dy[i]
#     if not (0<= nextx < w) or not(0 <= nexty < h) or c[nexty][nextx] == "#":
#       continue
#     if c[nexty][nextx] == "g":
#       print("Yes")
#       sys.exit()
#     dfs(nextx,nexty)
  
# dfs(sx,sy)

# print("No")

def dfs(stack):
  while (len(stack) >0):
    x, y = stack.pop()
    if not (0<= x < w) or not(0 <= y < h) or c[y][x] == "#":
      continue
    if c[y][x] == "g":
      print("Yes")
      sys.exit()
    
    c[y][x] = "#"
    stack.appendleft([x+1,y])
    stack.appendleft([x-1,y])
    stack.appendleft([x,y+1])
    stack.appendleft([x,y-1])

stack = deque()
stack.appendleft([sx,sy])
dfs(stack)
print("No")
  
  


