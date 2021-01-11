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

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter


Q =int(input())

for i in range(Q):
  n, s = mapInt()
  
  a = listInt()
  

  right = 0
  ans = INF
  sumA = 0
  
  for left in range(n):
    while(right < n and sumA < s):
      sumA += a[right]
      right += 1
    
    # if right != n-1:
    #   sumA += a[right]
    #   right += 1
    if (sumA < s):
      break #これ以上 left を進めてもダメ
    ans = min(ans, right - left)
    
    if (right == left):
      right += 1
    else:
      sumA -= a[left]
  if ans == INF:
    print(0)
  else:
    print(ans)
  
