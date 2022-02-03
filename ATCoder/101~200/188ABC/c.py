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

n = int(input())

a = listInt()
b = []
for i in range(2 ** n):
  b.append([a[i], i+1])

for i in range(n-1):
  for j in range(2**(n-1)):
    if b[2*j][0] > b[2*j +1][0]:
      b[j] = b[2*j]
    else:
      b[j] = b[2*j + 1]
    
# print(b)
if b[0][0] > b[1][0]:
  print(b[1][1])
else:
  print(b[0][1])
# x = min(b[0][0], b[1][0])
# print(x[1])