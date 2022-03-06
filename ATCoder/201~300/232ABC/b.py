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
s = input()
t = input()
# h, w = mapInt()
# n, k = mapInt()
n = len(s)

al = string.ascii_lowercase
x = len(al)
k = ord(t[0]) - ord(s[0])
# if k < 0:
#   s, t = t, s
  # k = -k
# print(s,t,k,x)
for i in range(len(al)):
  ok = True
  for j in range(n):
    p = ord(s[j]) - ord("a")
    # q = ord(s[j]) - ord("a")
    if al[(p+i) % x] != t[j]:
      ok = False
  if ok:
    print("Yes")
    exit()
  
  # print(p)
  # if p > 0 and p != k:
  #   print("No")
  #   exit()
  # if p < 0 and ( abs(p) + k) % x + 1 != k:
  #   print("No")
  #   exit()
    
print("No")
