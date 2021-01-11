import sys

sys.setrecursionlimit(10**8)

w = int(input())
h = int(input())




maze =  [ list(map(int, input().split())) for i in range(h)]


dx = [-1,0,1,0]
dy= [0,1,0,-1]
def dfs(pos,count = 1):
  x, y = pos
  result = count
  for i in range(4):
    sx,sy = x,y
    sx += dx[i]
    sy += dy[i]
    if not (0<= sx < w) or not (0<= sy < h):
      continue
    if maze[sy][sx] == 0:
      continue
    if done[sy][sx]:
      continue
    done[sy][sx] = True
    result = max(result, dfs((sx,sy),count + 1))
    done[sy][sx] = False
    
  return result

ans = 0
for i in range(h):
  for j in range(w):
    if maze[i][j] == 1:
      done = [[ False for i in range(w)] for i in range(h)]
      done[i][j] = True
      result = dfs((j,i))
      # print(result)
      ans = max(ans, result)


print(ans)
  