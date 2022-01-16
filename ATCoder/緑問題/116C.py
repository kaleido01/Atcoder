# -*- coding: utf-8 -*-
import sys, getpass
import math, random
from math import factorial
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import Iterable
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


n = int(input())
h = listInt()
ends = sum(h)

if ends == 0:
  print(0)
  sys.exit()


left = 0
ans = 0
while left < n:
  find0 = True
  while find0:
    cnt = 0
    for i in range(left, n):
      # print(h[i])
      if h[i] != 0:
        cnt = 1
        h[i] -= 1
      else:
        find0 = False
        break
    ans += cnt
  #次のスタート地点を決める
  if h[left] == 0:
    left += 1
  # for i in range(left, n):
  #   if h[i] == 0:
  #     left = i + 1
  #     break
  # print("left", left)
    
print(ans)



# その区間の花の高さを揃える最初のcntを返す
# def dfs(r, l, cnt):
#     minh = INF
#     isEnd = False
#     while (not isEnd):
#       isEnd = False
#       for i in range(r, l):
#         if h[i] == 0:
#           cnt += dfs(r, i) + dfs(i+1, l)
#         else:
#           minh = min(minh, h[i])
#       cnt += minh
#       for i in range(r, l):
#         h[i] -= minh
    
#   return cnt

    

  
  