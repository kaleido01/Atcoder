import math
n = int(input())

p = list(map(int, input().split()))
q = list(map(int, input().split()))


isUsed = [ False for _ in range(n+1) ]

ans1 = 1
for i in range(n):
  v = p[i]
  count = 0
  for j in range(1,v):
    if not isUsed[j]:
      count +=1
  ans1 += count * math.factorial(n - i - 1)
  isUsed[v] = True

isUsed = [ False for _ in range(n+1) ]
ans2 = 1
for i in range(n):
  v = q[i]
  count = 0
  for j in range(1,v):
    if not isUsed[j]:
      count +=1
  # print("count",count)
  ans2 += count * math.factorial(n - i - 1)
  # print(v)
  isUsed[v] = True

print(abs(ans1-ans2))

  