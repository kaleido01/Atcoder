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

# n = int(input())
# s = input()
# h, w = mapInt()
n, m, p = mapInt()
g = [ [] for _ in range(n)]
for i in range(m):
  a, b, c = mapInt()
  a -=1
  b -=1
  g[a].append([c-p, b])
  g[b].append([c-p, a])

def bellmanford(edge, V, start=0):
    """ベルマンフォード法

    startノードを始点とし, 他のノードを終点として移動したとき, 通る辺のコストの和の最小値
    負辺が存在しても使える
    計算量はO(EV)

    Args:
        edge (list): ノードAからノードBに行くコストがXの時[A, B, X]. これを全ての辺についてまとめたリスト
        V (int): ノード総数
        start (int, optional): 始点のノード. Defaults to 0.

    Returns:
        list or -1: 負の閉路が存在しないとき
                        startノードから[0番目のノードに移動するコストの最小値, 1番目のノードに移動するコストの最小値, ...]
                        dist[start] = 0
                    負の閉路が存在するとき
                        -1
    """
    INF = 1<<60
    dist = [INF] * V
    dist[start] = 0

    for i in range(V):
        for from_node, to_node, cost  in edge:

            if dist[from_node] + cost < dist[to_node]:
                dist[to_node] = dist[from_node] + cost

                # V回目にも更新があったら負の閉路が存在する
                if i == V-1:
                    return -1

    return dist

bellmanford(g, n, 0)