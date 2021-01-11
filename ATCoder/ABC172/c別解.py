

n, m, k = map(int, input().split())


an = list(map(int, input().split()))
bn = list(map(int, input().split()))

# 読んだ本の合計時間
t = 0

for i in range(m):
  t += bn[i]
  
ans = 0
j = m


for i in range(n+1):
  while (j > 0 and t > k):
    j -= 1
    t -= bn[j]
    
  if t > k:
    break
  ans = max(ans, i + j)
  if i == n:
    break
  t += an[i]

print(ans)
