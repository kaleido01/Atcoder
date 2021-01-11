import sys
import math 
import heapq
# from collections import deque

sys.setrecursionlimit(10**8)

h,w = map(int, input().split())
ch,cw = map(int, input().split())
dh,dw = map(int, input().split())

maze = [ list(input())for _ in range(h)]
dp =  [ [-1 for _ in range(w)] for _ in range(h)]
done =  [ [False for _ in range(w)] for _ in range(h)]


dx = [-1, 0, 1, -1]
dy = [0, 1, 0, -1]


def solve(x,y,count = 0):
  for i in range(4):
    sx ,sy = x,y
    sx += dx[i]
    sy += dy[i]
    if not (0<= sx < w) or not (0<= sy < h):
      continue
    if maze[sy][sx] == "#":
      continue
    if sx == dw -1 and sy == dh -1:
      print(count)
      sys.exit()
    if done[sy][sx]:
      continue
    done[sy][sx] = True
    solve(sx,sy,count)
    # done[sy][sx] = False

    
  for i in range(-2, 3):
    for j in range(-2,3):
      if i == 0 and j == 0:
        continue
      sx ,sy = x,y
      sx += j
      sy += i
      if not (0<= sx < w) or not (0<= sy < h):
        continue
      if sx == dw -1 and sy == dh -1:
        print(count+1)
        sys.exit()
      if maze[sy][sx] == "#":
        continue
      if done[sy][sx]:
        continue
      done[sy][sx] =True
      solve(sx,sy,count + 1)
      # done[sy][sx] = False
  
  
dp[ch-1][cw-1] = 0
done[ch-1][cw-1] = True
solve(cw-1,ch-1,0)
# print(dp)
print(-1)
  