h, w, n, m = map(int, input().split())

# 上右下左
isCheckedlight = [[False, False, False, False] for i in range(n)]
done = [ [ False for i in range(w) ] for i in range(h)]

light = [ [ False for i in range(w) ] for i in range(h)]

# -1 は道 -2 は障害物 0以上はi番目のlightがあることを示す
maze = [ [ -1 for i in range(w) ] for i in range(h)]
# print(light)
# print(maze)
for i in range(n):
  y, x = map(int, input().split())
  x -= 1
  y -= 1
  # print(x,y)
  maze[y][x] = i
  

for i in range(m):
  y, x = map(int, input().split())
  x -= 1
  y -= 1
  
  maze[y][x] = -2



dx = [0 ,1 ,0, -1]
dy = [1 ,0 ,-1, 0]
# for i in range(n):
#   x, y = light[i]
#   # print("x,y",x,y)
#   for j in range(4):
#     direction = isCheckedlight[i]
#     if not direction[j]:
#       # print(done)
#       sx, sy = x,y
#       done[y][x] = True
#       while(True):
#         sx += dx[j]
#         sy += dy[j]
#         if not (0 <= sx < w) or not (0<= sy < h):
#           break
#         if maze[sy][sx] == -2:
#           break
#         if maze[sy][sx] >=0:
#           lightIndex = maze[sy][sx]
#           if lightIndex == 0 or lightIndex == 2:
#             isCheckedlight[lightIndex][0] = True
#             isCheckedlight[lightIndex][2] = True
#           else:
#             isCheckedlight[lightIndex][1] = True
#             isCheckedlight[lightIndex][3] = True
#         done[sy][sx] = True
        
      
      
      
      
ans = 0
for i in range(h):
  for j in range(w):
    if done[i][j]:
      ans += 1
      
print(ans)