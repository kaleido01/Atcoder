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

n, d = mapInt()

l = []
for i in range(n):
  l.append(listInt())
  
  
l.sort(key= lambda array: array[1])

# print(l)
ans = 0

pt = 0


def overlap(left, right, segment):
  nl, nr = segment
  
  if right <= nl <= right+d - 1: return True
  if right <= nr <= right+d - 1: return True
  if nl <= right and right+d-1 <= nr : return True
  return False


while(pt < n):
  left, right = l[pt]
  
  while(pt < n and overlap(left, right, l[pt])):
    pt += 1
  
  ans +=1
  
print(ans)
