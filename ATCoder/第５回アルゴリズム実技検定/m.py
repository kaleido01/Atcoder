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


n, l = mapInt()

maxL= 10 ** 15

a = listInt()
minl = max(a)

def isOk(baundary):
  limit = 0
  print("baundary",baundary)
  # maruta
  for i in range(n):
    limit += a[i]
    if limit >= baundary:
      # print(limit)
      if i != n-1:
        limit = 0

  if limit < baundary:
    return False
  return True

def binary_search():
  ok = minl
  ng = l
  
  while(abs(ng - ok) >1):
    # middle = left + (left - right)//2
    middle = (ok + ng)//2
    if isOk(middle):
      ok = middle
    else:
      ng = middle
  return ok
      
ans = binary_search()
  
  
print(ans)
  
  
