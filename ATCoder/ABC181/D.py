import sys
from itertools import permutations
s = int(input())





# q = str(s)
# l = [i for i in q]

# patern = permutations(l)

# for v in patern:
#   x=""
#   for v2 in v:
#     x += v2
    
#   if int(x) % 8 == 0:
#     print("Yes")
#     sys.exit()
# print("No")


count = [0] * 10

for v in str(s):
  count[int(v)] +=1
  
  
if count[0] >=3:
  print("Yes")
  sys.exit()



for i in range(1,1000):
  if i % 8 == 0:
    count2 = [0] * 10
    for v in str(i):
      count2[int(v)] +=1
    if i <10:
      if count[0] >=2 and count[8]>=1:
        print("Yes")
        sys.exit()
    elif 10 <= i < 100:
      flag = True
      if count[0] >=1:
        for i in range(1, len(count2)):
          if count[i] < count2[i]:
            flag = False
        if flag:
          print("Yes")
          sys.exit()
    else:
      flag = True
      
      for i in range(len(count2)):
        if count[i] < count2[i]:
          flag = False
      
      if flag:
        print("Yes")
        sys.exit()
    
    
      
            
        

# keta = 1
# p = s
# while(p //10 != 0):
#   keta +=1
#   p //=10
  
   
# print(10**(keta-1), 10**keta)
# for i in range(10**(keta-1) ,10**keta):
#   if i % 8 == 0:
#     count2 = [0] * 10
#     for v in str(i):
#       count2[int(v)] +=1
#       flag = True
#       # print(count, count2)
#     for j in range(9):
#       if count[j] != count2[j]:
#         flag = False
#     if flag:
#       # print(count, count2)
#       print("Yes")
#       sys.exit()

print("No")
    
