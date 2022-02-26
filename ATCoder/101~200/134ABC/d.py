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

n = int(input())
# s = input()
# h, w = mapInt()
# n, k = mapInt()

a = listInt()
ball = [0] * (n+1)
# for i in range(1, n+1):
#   for j in range(i, n+1, i):
#     cnt[j].append(i)
    

can = True
ans = []
ansCnt = 0
# 上から確定させる
for i in range(n, 0, -1):
  cnt = 0
  #ここまでの倍数で確定したボールの数を数える
  for j in range(i, n+1, i):
    cnt += ball[j]
  # print(cnt, a[i-1])
  if cnt % 2 != a[i-1]:
    ans.append(i)
    ball[i] +=1
    ansCnt +=1
  
# print(cnt)
# if not can:
#   print(-1)
#   exit()
print(ansCnt)
if ansCnt > 0:
  print(*ans)