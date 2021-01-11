from collections import deque

w, h= map(int, input().split())

maze = [list(map(int,input().split())) for _ in range(h)]

maze.insert(0,[0] * (w+2))
maze.append([0] * (w+2))
for i in range(1, h+1):
  maze[i].insert(0,0)
  maze[i].append(0)
  
done = [[False for _ in range(w+2)]for _ in range(h + 2)]

que = deque()
que.append((0,0))
done[0][0] = True

evenDx =[-1, 0, -1,1, -1,0]
evenDy =[-1, -1, 0, 0, 1,1]
oddDx =[0, 1, -1,1, 0,1]
oddDy =[-1, -1, 0,0, 1,1]

while (len(que) >.0):
  x, y= que.popleft()

  for i in range(6):
    ux,uy = x, y
    if y % 2 == 0:
      ux += evenDx[i]
      uy += evenDy[i]
    else:
      ux += oddDx[i]
      uy += oddDy[i]
    if not (0 <= ux <= w + 1) or not (0<= uy <= h + 1):
      continue
    if maze[uy][ux] ==1:
      continue
    if done[uy][ux]:
      continue
    done[uy][ux] = True
    que.append((ux,uy))

# print(done)
count = 0
for i in range(1,h+1):
  for j in range(1, w+1):
    if not done[i][j]:
      for k in range(6):
        ux,uy = j,i
        if i % 2 == 0:
          ux += evenDx[k]
          uy += evenDy[k]
        if i % 2 == 1:
          ux += oddDx[k]
          uy += oddDy[k]
        if done[uy][ux]:
          count +=1
print(count)

