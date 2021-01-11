

n, m, k = map(int, input().split())


an = list(map(int, input().split()))
bn = list(map(int, input().split()))

counter = 0
sn =[0]* (n+1)
sm =[0]* (m+1)
for i in range(n):
  sn[i+1]= sn[i] +an[i]
for i in range(m):
  sm[i+1]= sm[i] +bn[i]
  
  
ans = 0
j = m

while (True):
  if sm[j] > k:
    j -= 1
  else:
    break

for i in range(n+1):
  if j == -1:
    break
  if sm[j] + sn[i] <= k:
    ans = max(ans,j + i)
    i += 1
  else:
    while (True):
      if j == -1:
        break
      if sm[j] + sn[i] <= k:
        
        ans = max(ans,j + i)
        break
      else:
        j -= 1

print(ans)
    
  
  


# for i in range(n+m):
  
#   if len(an) == 0 and len(bn) == 0:
#     break
#   if len(an) == 0:
#     if sumTime + bn[0] <= k:
#       sumTime += bn[0]
#       bn.pop(0)
#       counter += 1
#   elif len(bn) == 0:
#     if sumTime + an[0] <= k:
#       sumTime += an[0]
#       an.pop(0)
#       counter += 1
#   elif an[0] >= bn[0] and sumTime + bn[0] <= k:
#     sumTime += bn[0]
#     bn.pop(0)
#     counter += 1
#   elif an[0] <= bn[0] and sumTime + an[0] <= k:
#     sumTime += an[0]
#     an.pop(0)
#     counter += 1
#   else:
#     break
  
#   print(an)
#   print(bn)

# print(counter)