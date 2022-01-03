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

q = intInput()

stack = {}

start = 0
end = 1
for i in range(q):
  t, x = mapInt()
  if t == 1:
    stack[start] = x
    start -= 1
  elif t == 2:
    stack[end] = x
    end += 1
  else:
    print(stack[start+x])
    
    
# 別解ライヴラリを使う
# deck = deque()
# for _ in range(Q):
#     t, x = map(int, stdin.readline().split())
#     if t == 1:
#         deck.appendleft(x)
#     elif t == 2:
#         deck.append(x)
#     elif t == 3:
#         print(deck[x-1])