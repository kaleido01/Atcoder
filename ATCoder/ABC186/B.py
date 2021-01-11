import math
h,w = map(int, input().split())

x = [list(map(int, input().split())) for i in range(h)]

minval = math.inf
for i in range(h):
  for j in range(w):
    minval = min(minval, x[i][j])
    
ans = 0

for i in range(h):
  for j in range(w):
    ans += x[i][j] - minval 



print(ans)