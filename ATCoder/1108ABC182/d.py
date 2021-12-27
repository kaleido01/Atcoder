n = int(input())

a = list(map(int,input().split()))

# 1111   6666        8888888
a.sort()[-1]


print(a)
# s = [0] * (n+1)

# for i in range(n):
#   s[i+1] = s[i] + a[i]
 

# maxIndex = 0
# maxV = [0] * (n+1)
# maxS =0 
# k = [0] * (n+1)
# for i in range(n):
#   maxS = max(maxS, s[i+1])
#   maxV[i] = k[i] + maxS
#   k[i+1] = k[i] + s[i+1]
  
# # print(maxIndex)
# print(max(maxV))

