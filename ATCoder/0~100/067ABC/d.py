# -*- coding: utf-8 -*-
from cmath import cos
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

g = [ [] for i in range(n)]
for i in range(n-1):
    a, b = mapInt()
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
    
    
q = deque()

fill = [-1] * n

fill[0] = 1
fill[n-1] = 0
q.append((0,1))
q.append((n-1,0))

while q:
    pos, me = q.popleft()
    nodes = g[pos]
    
    for node in nodes:
        if fill[node] != -1: continue
        fill[node] = me
        q.append((node, me))
        
        

cntF = 0
cntS = 0 

for i in range(n):
    if fill[i]:
        cntF +=1
    else:
        cntS +=1
if cntF > cntS:
    print("Fennec")
else:
    print("Snuke")
    