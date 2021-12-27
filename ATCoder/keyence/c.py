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
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter
from collections import deque
import heapq

n = int(input())
 
a = listInt()
b = listInt()

x = [0] * n
res = 0
count = 0
for i in range(n):
  x[i] = a[i] -b[i]
  if x[i] < 0:
    res+= x[i]
  else:
    count += 1

x.sort(reverse = True)
# print(x)

if count == n:
  print(0)
  sys.exit()

for i in range(n):
  if x[i] < 0:
    print(-1)
    sys.exit()
  res += x[i]
  if res >=0:
    print(n - (count - i -1))
    sys.exit()



