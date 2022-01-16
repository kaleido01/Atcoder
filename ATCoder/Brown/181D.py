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


# s = input()


# if int(s) < 10:
#   YesNo(int(s) % 8 == 0)
#   sys.exit()
    

# cnt = [0] * 10

# for x in s:
#   cnt[int(x)] += 1
  
# ans = False
# m = 1000
# p = 100
# if int(s)< 100:
#   m = 100
#   p = 10
# for i in range(p, m):
#   cnt2 = [0] * 10
#   flag = True
#   if i % 8 == 0:
#     x = str(i)
#     for xx in x:
#       cnt2[int(xx)] += 1
#     # print(cnt2)
#     for j in range(10):
#       if cnt[j] < cnt2[j]:
#         flag = False
#   else: flag = False
  
#   if flag:
#     ans = True
# # print(cnt)
# YesNo(ans)
from collections import Counter, defaultdict, deque
s = input()
if len(s) <= 2:
  if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
    YesNo(True)
  else:
    YesNo(False)
  sys.exit()

cnt = Counter(s)

for i in range(112, 1000, 8):
  # print(Counter(str(i)))
  if not Counter(str(i)) - cnt:
    print("Yes")
    sys.exit()
print("No")


# print(Counter("123") - Counter("1234"))