# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input())for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from itertools import combinations, permutations, combinations_with_replacement


n, m = mapInt()

a = [] * m

for i in range(m):
  a.append(listInt())
  

def count2(x):
  count = 0
  for i in range(3):
    if a[x][i] in checkList:
      count += 1
    
  return count

ans = 0
for i in range(1 << n):
  isOK = True
  now = []
  checkList=[]
  for j in range(n):
    
    if i >> j & 1:
      checkList.append(j+1)
  # if len(checkList) <=1:
  #   continue
  for j in range(m):

    count = count2(j)
    # print(count)
    if count == 3:
      isOK =False
      break
    elif count == 2:
      for k in range(3):
        if a[j][k] not in checkList:
          if a[j][k] not in now:
            now.append(a[j][k])
    
  if isOK:
    # print(checkList)
    # print(now)
    ans = max(ans, len(now))

      
print(ans)
    
# #組み合わせパターン生成
# c_list = list(combinations(range(1,n+1), 2))
# print(c_list)
# # print(c_list)
# ans = 0

# for c in c_list:
#   now = []
#   for i in range(m):
#     x, y = c[0], c[1]
#     count = 0
    
#     if x in a[i]:
#       count += 1
#     if y in a[i]:
#       count += 1
#     if count == 2:
#       for j in range(3):
#         if a[i][j] != x and a[i][j] != y:
#           if a[i][j] not in now:
#             now.append(a[i][j])
#   print(now)
#   ans = max(len(now), ans)

    
# print(ans)