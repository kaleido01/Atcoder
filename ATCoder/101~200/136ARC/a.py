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
s = list(input())

i = 0
ans = []
q = deque()
while(i < n):
  if s[i] == "C": 
    ans.append("C")
    i +=1
    continue
  
  if s[i] == "A":
    ans.append("A")
    i +=1
    continue
  
  if s[i] == "B":
    if i < n-1:
      if s[i+1] == "A":
        s[i], s[i+1] = s[i+1], s[i]
        ans.append("A")
        i += 1
      elif s[i+1] == "B":
        ans.append("A")
        i+=2
      else:
        ans.append("B")
        i+=1
    else:
        ans.append("B")
        i+=1
        
print("".join(ans))