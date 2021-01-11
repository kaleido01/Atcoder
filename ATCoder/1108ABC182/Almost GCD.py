n = int(input())

a=[v for v in list(map(int, input().split()))]

print(a)
m = 0
sum = 0
ans = 0
for i in range(2,1001):
    for j in range(n):
      if a[j] % i == 0:
        sum +=1
    if m < sum:
      m = max(m, sum)
      ans = i
    sum = 0
  
print(ans)