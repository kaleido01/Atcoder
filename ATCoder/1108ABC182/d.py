n = int(input())

a = list(map(int,input().split()))


s = [0] * (n+1)

for i in range(n):
  s[i+1] = s[i] + a[i]
 

maxIndex = 0
maxV = [0] * (n+1)
maxS =0 
k = [0] * (n+1)
for i in range(n):
  maxS = max(maxS, s[i+1])
  maxV[i] = k[i] + maxS
  k[i+1] = k[i] + s[i+1]
  
# print(maxIndex)
print(max(maxV))
# print (s,k)
# if maxIndex == 0:
#   print(0)
# elif maxIndex == n:
#   print(k[maxIndex] + max(s[:maxIndex+1]))
# else:
#   print(k[maxIndex] + max(s[:maxIndex+2]))
