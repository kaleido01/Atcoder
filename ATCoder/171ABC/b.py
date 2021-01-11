n, k = map(int, input().split())

an = list(map(int, input().split()))

an.sort()


ans = 0

for i in range(k):
  ans+= an[i]
  
  
print(ans)