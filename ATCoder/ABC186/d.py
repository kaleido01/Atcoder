n = int(input())
an = list(map(int, input().split()))


sum = 0

an.sort()

for i in range(n):
  sum += (2*i-n +1)* an[i]
  
print(sum)