# -*- coding: utf-8 -*-
from re import L
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

n = int(input())

inp = []
ta = -INF
ba = INF
for i in range(n):
  z  = list(input().split())
  o, x, y, a = z[0], int(z[1]), int(z[2]), int(z[3])
  ta = max(ta, y)
  ba = min(ba, y-a+1)
  inp.append([o, x, y, a])
  
print(ba, ta)
ans = 0
for i in range(ba-1, ta, 1):
  before = []
  op = []
  for j in range(n):
    o, x, y, a = inp[j]
    if not(y-a <= i <= a): continue
    before.append(x)
    before.append(x + a)
    op.append(o == "+")
      
  # 集合型にすることで重複を除去し、
  # 小さい順にソートする
  B = sorted(set(before))

  # B の各要素が何番目の要素なのかを辞書型で管理する
  D = { v: i for i, v in enumerate(B) }

  # 答え
  after = list(map(lambda v: D[v], before))
  cnt = len(before)
  s = [0] * cnt
  
  # +ならその区間 = 1, -ならその区間 = 0
  for i in range(len(op)):
    left, right = after[2*i], after[2*i+1]
    for j in range(left, right+1):
      if op[i]:
        s[j] = 1
      else:
        s[j] = 0

  # 0->1 1->0 1->1 になってる区間を足し合わせる
  print("test", before, after, s)
  for i in range(len(s)-1):
    if s[i] == 0 and s[i+1] == 0: continue
    # if s[i] == 1 and s[i+1] == 0: continue
    left = 0
    right = 0
    for j in range(cnt):
      if after[j] == i:
        left = before[j]
      elif after[j] == i+1:
        right = before[j]
    print(left, right)
    ans += right - left
    if s[i] == 1 and s[i+1] == 1:
      ans +=1
      
print(ans)