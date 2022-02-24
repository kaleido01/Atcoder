# -*- coding: utf-8 -*-
from lib2to3.pgen2.token import INDENT
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
a = listInt()

s = [0] * (n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]

ansA = 0

# 全体でどれだけ+されているか
temp = 0
# + - + -
for i in range(1, n+1):
    if i % 2 == 1:
        if s[i] + temp<= 0:
            ansA += 1 - (s[i] + temp)
            temp += 1 - (s[i] + temp)
    else:
        if s[i] + temp>= 0:
            ansA += s[i] + temp + 1
            temp -= s[i] + temp + 1
            
            
            
ansB = 0
temp = 0
# - + - +
for i in range(1, n+1):
    if i % 2 == 0:
        if s[i] + temp <= 0:
            ansB += 1 - (s[i] + temp)
            temp += 1 - (s[i] + temp)
    else:
        if s[i] + temp >= 0:
            ansB += s[i] + temp + 1
            temp -= s[i] + temp + 1
            
            
# print(s)
# print(ansA, ansB)
print(min(ansA, ansB))
            
            