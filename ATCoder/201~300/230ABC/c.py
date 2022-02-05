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
p = []

for i in range(n):
  p.append(listInt())
  
  
count = 0
for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      p1, p2, p3 = p[i], p[j], p[k]
      x1, y1, x2, y2, x3, y3 = p1, p2, p3
      if (y2-y1) / (x2-x1) and (y3-y2)/(x3-x2):
        count +=1
        
print(n * (n-1) * (n-2) / 6 - count)
      