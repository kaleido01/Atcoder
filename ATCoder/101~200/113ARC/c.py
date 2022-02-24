# -*- coding: utf-8 -*-
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7 # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
init1 = lambda n: [-1 for _ in range(n)]
initAny = lambda n, a: [a for _ in range(n)]


inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

s = list(input())
s.reverse()
n = len(s)

asci = string.ascii_lowercase
a = {}
# for k in asci:
#   x = [0] * (n+1)
#   for i in range(n):
#     x[i+1] = x[i]
#     if s[i] == k:
#       x[i+1] +=1
#   a[k] = x


def isOk(i):
  return s[i] == s[i+1], s[i]


ans = 0
last = ""
left = 0
# for i in range(n-1):
#   if last == s[i]:
#     continue
#   else:
#     if s[i-1] == s[i-2] != s[i]:
#       left = i
#       last = s[i]
#   ok, key = isOk(i)
#   print(ok,key)
#   if ok:
#     # print(a[key], left)
#     print(i, a[key][i], a[key][left-1])
#     ans += i - (a[key][i] - (a[key][left]))
#     last = key
#     # left = i
    
for i in range(n-1):
  ok, key = isOk(i)
  if ok:
    if key in a:
      ans += i - a[key]
    else:
      ans += i
    a = {}
    a[key] = i+1
  else:
    if key in a:
      a[key] +=1
    else:
      a[key] =1
      
  
print(ans)


for i in range(1, 20):
  print(20)
print(1)