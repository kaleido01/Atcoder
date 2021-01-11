import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限

def search(x,y):
  
  if not(0<= x < w) or not(0<= y < h):
    return
  if island[y][x] == 0:
    return
  
  island[y][x] = 0
  
  # 8方向探索
  search(x-1,y+1)
  search(x,y+1)
  search(x+1,y+1)
  search(x+1,y)
  search(x+1,y-1)
  search(x,y-1)
  search(x-1,y-1)
  search(x-1,y)

while(True):
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  island = [list(map(int, input().split())) for _ in range(h)]
  count = 0
  for i in range(h):
    for j in range(w):
      if island[i][j]:
        count +=1
        search(j,i)
  print(count)
