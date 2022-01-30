# -*- coding: utf-8 -*-
from re import L
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
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

inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(map(int, input().split())) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N, D = mapInt()
a = listInt()

comb = [] * (1 << N)

for i in range(1 << N):
  c = []
  for j in range(N):
    if (i >> j) & 1:
      c.append(a[j])
  comb.append(c)

f = [0] * (1 << N)
# for i in range(1 << N):
#   cnt = 0
#   for bit in range(D):
#     ok = True
#     for j in range(N):
#       if (i >> j) & 1:
#         x = a[j]
#         if (x >> bit) & 1:
#           ok = False
#     if ok: cnt += 1
    
#   f[i] = cnt

# print(comb)
for i in range(1 << N):
  c = comb[i]
  cnt = 0
  temp = 0
  # 全てのxとの論理和を取る。この時、桁が０になった場合は、xの中のその桁に１が一つも存在しなかったということ。
  # 愚直に桁ごとに計算してしまうと(N * D になってしまうので全部の論理和をとってまとめて処理することで論理和でN回, 各桁の確認でD回のN + D回に抑える）
  for x in c:
    temp |= x
  for d in range(D):
    if not (temp >> d) & 1:
      cnt +=1
  f[i] = cnt
    

ans = 0
for i in range(1 << N):
  cnt = 0
  for j in range(N):
    if (i >> j) & 1:
      cnt += 1
      
  if cnt % 2 == 0:
    ans += 2 ** f[i]
  else:
    ans -= 2 ** f[i]
    
# print(f)
print(ans)