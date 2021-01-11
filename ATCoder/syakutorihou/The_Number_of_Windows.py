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

# n, q = mapInt()

# a = listInt()
# Q = listInt()

n, q = map(int, input().split())
a = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]

for limx in Q:
  
  ans = 0
  vol = 0
  right = 0
  
  for left in range(n):
    while( right < n and vol + a[right] <= limx ):
      vol += a[right]
      right += 1
      
    ans += right - left
    
    if left - right == 0:
      right += 1
    else :
      vol -= a[left]
    

  print(ans)
      
    
    
    