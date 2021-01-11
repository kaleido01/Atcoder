n,m = map(int, input().split())

a = [0] * n

for i in range(n-1):
  s = int(input())
  a[i+1] += a[i] + s
  
position=0
ans = 0

for i in range(m):
  s = int(input())
  position += s
  ans += abs(a[position] - a[position - s]) % 10**5


print(ans % 10 **5)