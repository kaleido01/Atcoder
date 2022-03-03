# -*- coding: utf-8 -*-
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(3*10**5+10)
INF=1 << 50
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
# h, w = mapInt()

V, E = map(int,input().split())    # Vは頂点数、Eは辺数
es = []    # 辺
for _ in range(E):
    # 頂点fromから頂点toへのコストcostの辺
    f, t, c = map(int,input().split())
    f -=1
    t -=1
    es.append([f, t, -c])

def bellmanford(s):
    d = [INF] * V
    d[s] = 0
    negative = [False] * V
    for i in range(V):
        for j in range(E):
            e = es[j]
            if d[e[0]] == INF: continue
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                # n回目にも更新があるなら負の経路が存在する
                if i == V-1:
                    # 行き先が更新されたので、行き先が負のループの対象。
                    negative[e[1]] = True
                    d[e[1]] = -INF
    for i in range(V):
        for j in range(E):
            e = es[j]
            if d[e[0]] == INF: continue
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
            # 自身から行ける場所e[0] -> e[1] は全て負のループ
            if negative[e[0]]:
              negative[e[1]] = True
              d[e[1]] = -INF
    
    
    return d

d = bellmanford(0)    # 頂点0を始点とする

if d[V-1] == -INF:
  print("inf")
else:
  print(-d[V-1])