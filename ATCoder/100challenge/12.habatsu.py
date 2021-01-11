from itertools import combinations
n, m = map(int, input().split())

dic ={}

for i in range(m):
  x, y = map(int, input().split())
  s = str(x) + str(y)
  dic[s]= True

# def binary(v):
#   i=0
#   bit= [0] *13
#   while (v>0):
#     bit[i] = v%2
#     i +=1
#     v //=2
#   return bit

ans = 1
# bit演算なし
# for i in range (2 ** n):
#   bit = binary(i)
#   # print(bit)
#   l=[]
#   for bitIn in range(len(bit)):
#     if bit[bitIn] == 1:
#       l.append(bitIn+1)
#   checks=list(combinations(l,2))
#   isExist = True
#   for check in checks:
#     x,y = check
#     s = str(x) + str(y)
#     if s not in dic:
#       isExist = False
#   if isExist:
#     ans = max(ans, len(l))

#bit演算あり
for i in range(2**n):
  l=[]
  for j in range(n):
    if (i >> j) & 1 :
      l.append(j+1)
  checks=list(combinations(l,2))
  isExist = True
  for check in checks:
    x,y = check
    s = str(x) + str(y)
    if s not in dic:
      isExist = False
  if isExist:
    ans = max(ans, len(l))
    
print(ans)