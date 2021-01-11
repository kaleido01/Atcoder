n, m = map(int, input().split())

a = []

for i in range(n):
  a.append([ v for v in list(map(int, input().split()))])
  
s= [0] * n
ans =0

for i in range(m-1):
  for j in range(i+1, m):
    for x in range (1,n+1):
      s[x-1] = max(a[x-1][i], a[x-1][j])
    ans = max(ans,sum(s))

print(ans)