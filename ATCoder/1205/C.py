import sys
n = int(input())
p = list(map(int, input().split()))


ans=[]
done=[False] * (n-1)
value = 1
count =0
while(value <=n-1):
  nextIndex= p.index(value)
  value = nextIndex+2
  # print(p)
  for j in range(nextIndex,p[nextIndex]-1, -1):
    if done[j-1] == True:
      print(-1)
      sys.exit()
    else:
      done[j-1] = True
      ans.append(j)
      p[j-1], p[j] = p[j], p[j-1]
      count += 1

# print(count)
# print(p)
for i in range(len(p)):
  if p[i] == i+1:
    print(-1)
    
    sys.exit()
    
for v in ans:
  print(v)
  
