# -*- coding: utf-8 -*-
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
intInput = lambda: int(input())
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


# n = int(input())
# s = input()

# temp = 0
# right = 0
# l = 0
# r = 0
# for i in range(n):
#   if s[i] == "(":
#     if right != 0:
#       if temp > right:
#         r += temp-right
#       elif temp < right:
#         l += right -temp
#       temp = 0
#       right = 0
#     temp += 1
#   else:
#     right += 1

# if temp > right:
#   r += temp-right
# elif temp < right:
#   l += right -temp


# ans = "(" * l + s + ")" * r
# print(ans)


n = int(input())
s = input()

cnt = 0
pre = 0

for i in range(n):
  if s[i] == "(":
    cnt += 1
  else:
    cnt -= 1
  if cnt < 0:
    pre = max(pre, abs(cnt))
    

if pre > 0:
  s  = "(" * pre + s


cnt = 0
for i in range(len(s)):
  if s[i] == "(":
    cnt += 1
  else:
    cnt -= 1
    

s = s + ")" * abs(cnt)
print(s)