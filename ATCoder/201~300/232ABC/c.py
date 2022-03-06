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
n, m = mapInt()


ao = [ [] for i in range(n)]
suzu = [ [] for i in range(n)]
for i in range(m):
  a, b = mapInt()
  a -=1
  b-= 1
  ao[a].append(b)
  ao[b].append(a)
for i in range(m):
  a, b = mapInt()
  a -=1
  b-= 1
  suzu[a].append(b)
  suzu[b].append(a)
  

l = [  i for i in range(n)]
pattern = list(itertools.permutations(l, n))

for p in pattern:
  temp = [ [] for i in range(n)]
  for i in range(n):
    nodes = suzu[i]
    for node in nodes:
      temp[p[i]].append(p[node])

  # tempがaoに一致するか
  # print(ao, temp)
  ok = True
  for i in range(n):
    k = sorted(temp[i])
    l = sorted(ao[i])
    # print("aaaa", k,l)
    if k != l:
      ok = False
  if ok:
    print("Yes")
    exit()

print("No")


