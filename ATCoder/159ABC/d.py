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
inithw = lambda h, w: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter

n = int(input())

a = listInt()

maxN= 2 * 10**5 +1
l =[0 for i in range(maxN)]


for i in range(n):
  l[a[i]] += 1
  
allAns = 0

for i in range(len(l)):
  x = l[i]
  if x >= 2:
    allAns += x * (x-1) //2

# print(l[0:10])
# print(allAns)
for i in range(n):
  removeV = a[i]
  ans = allAns
  x = l[removeV]
  u = x * (x-1) //2
  x -= 1
  v = x * (x-1) //2
  if x == 1:
    print(ans - 1)
  else:
    print(ans -  (u - v) )
    