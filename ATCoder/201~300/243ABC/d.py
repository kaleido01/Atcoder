# -*- coding: utf-8 -*-
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(3*10**5+10)
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

# n = int(input())
# s = input()
# h, w = mapInt()
n, x = mapInt()
s = input()

temp = x
# for i in range(n):
#   if s[i] == "U":
#     temp //= 2
#   elif s[i] == "R":
#     temp = temp*2+1
#   else:
#     temp = temp*2
#   # print(temp)
# print(temp)

cnt = 0
for i in range(n):
  new = 0
  if cnt > 0:
    if s[i] == "U":
      cnt -= 1
    else:
      cnt += 1
    continue
  # if cnt > 0: continue
    
  if s[i] == "U":
    new = temp // 2
  elif s[i] == "R":
    new = temp*2 +1
  else:
    new = temp*2
    
  if new <= 10**18:
    temp = new
  else:
    cnt +=1
  
print(temp)