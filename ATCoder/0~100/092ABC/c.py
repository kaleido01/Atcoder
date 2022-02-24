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
a.insert(0,0)
a.insert(n+1,0)
s = 0
b = []
for i in range(1, n+2):
  s += abs(a[i] - a[i-1])

# print(s)
for p in range(1, n+1):
  temp = s
  temp -= abs(a[p] - a[p-1])
  temp -= abs(a[p+1] - a[p])
  temp += abs(a[p+1] - a[p-1])
  print(temp)
  
