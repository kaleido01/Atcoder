# -*- coding: utf-8 -*-
from re import L
import sys, getpass
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

n = int(input())
s = list(input())
# s += s
# print(s)
ans = [""] * n
if s[0] == "o":
  ans[0] = "S"
  ans[1] = "S"
  ans[-1] = "S"
else:
  ans[0] = "W"
  ans[1] = "W"
  ans[-1] = "W"
  

def check(index, b):
  r = 0
  t = 0
  if b:
    r = index
    t = 1
  else:
    r = n - index
    t = -1
  if ans[r] == "S" and s[r] == "o":
      ans[r+t] = "S"
  elif ans[r] == "S" and s[r] == "x":
    if index == 1 and not b:
      if ans[0] == "W":
        ans[r+t] = "S"
      else:
        ans[r+t] = "W"
    else:
      if ans[r-t] == "W":
        ans[r+t] = "S"
      else:
        ans[r+t] = "W"
  elif ans[r] == "W" and s[r] == "x":
    ans[r+t] = "W"
  else:
    if ans[r-t] == "W":
      ans[r+t] = "S"
    else:
      ans[r+t] = "W"


end = n // 2
temp = []
for i in range(1, end+2):
  
  # 右方向
  check(i, True)
  if end+1 == i:
    temp = ans.copy()
  check(i, False)
  # print(temp, ans)
  if end+1 == i:
    if "".join(temp) == "".join(ans):
      print("".join(ans))
    else:
      print(-1)
  

# for i in range(n):
#   if i == 0:
#     if s[i] == "o"
# print(end)
# print(ans)
    
    
    