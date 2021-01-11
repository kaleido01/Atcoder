n = int(input())


c = [0 for _ in range(10 ** 6 +5)]

for i in range(n):
  x,y = map(int, input().split())
  c[x] +=1
  c[y+1] -=1

s = [0 for _ in range(10 ** 6 +7)]

for i in range(len(c)):
  s[i+1] = s[i] + c[i]
  
  
print(max(s))