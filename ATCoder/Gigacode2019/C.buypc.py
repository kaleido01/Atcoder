import math
d = int(input())

an = list(map(int, input().split()))
bn = list(map(int, input().split()))

ans = math.inf
money = 0
for i in range(d):
  money += an[i]
  if money >= bn[i]:
    ans = min(ans, bn[i])
    
if ans == math.inf:
  print(-1)
else:
  print(ans)