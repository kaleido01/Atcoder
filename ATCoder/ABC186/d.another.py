n = int(input())
an = list(map(int, input().split()))

ans = 0
s = [0] * (n+1)

an.sort()

for i in range(n):
  s[i+1] = s[i] + an[i]
  
print(s)
for i in range(n-1):
  ans -= (n-i-1) * an[i]
  ans += s[n]-s[i+1]
  

print(ans)