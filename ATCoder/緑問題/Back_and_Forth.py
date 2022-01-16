# -*- coding: utf-8 -*-
import sys
import getpass
import math
import random
import functools
import itertools
import collections
import heapq
import bisect
from collections import Counter, defaultdict, deque
from typing import Deque
sys.setrecursionlimit(10**9)
INF = 10**18
MOD = 10**9+7  # 998244353
d4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout


def input(): return sys.stdin.readline().rstrip()


def intInput(): return int(input())


def mapInt(): return map(int, input().split())


def listInt(): return list(map(int, input().split()))


def init0(n): return [0 for _ in range(n)]


def inithwv(h, w, v): return [[v for _ in range(w)] for _ in range(h)]


def inithw(h): return [list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]


def initDp(n): return [[] for _ in range(n)]


def bit(n, k): return ((n >> k) & 1)  # nのkビット目


def YesNo(b): return bool([print('Yes')] if b else print('No'))


def YESNO(b): return bool([print('YES')] if b else print('NO'))


def int1(x): return int(x)-1


sx, sy, tx, ty = mapInt()
# sx += 1000
# sy += 1000
# tx += 1000
# ty += 1000


# minx = -1000
# maxx = 1000
# m = maxx - minx + 1

# que = Deque()


# done = [[False for _ in range(m)] for _ in range(m)]


# def dfs(last):
#     lx, ly = last
#     # print(que)
#     while que:
#         cx, cy, cur = que.popleft()
#         # print(cx, cy, cur)
#         if cx == lx and cy == ly:
#             # print(cx, cy, cur)
#             return cur

#         for i in range(4):
#           dx, dy = d4[i]
#           xx = cx + dx
#           yy = cy + dy

#           if not(0 <= xx < m and 0 <= yy < m):
#               continue
#           if done[xx][yy]:
#               continue
#           done[xx][yy] = True

#           temp = ""
#           t = cur.copy()
#           if i == 0:
#               temp = "R"
#           elif i == 1:
#               temp = "U"
#           elif i == 2:
#               temp = "L"
#           elif i == 3:
#               temp = "D"
#           t.append(temp)
#           # print(temp, ncur)
#           que.append((xx, yy, t))


# def reset(start, fill):
#   x, y = start

#   for s in fill:
#     if s == "U":
#         y += 1
#     if s == "R":
#         x += 1
#     if s == "D":
#         y -= 1
#     if s == "L":
#         x -= 1
#     done[x][y] = True


# que.append([sx, sy, []])
# done[sx][sy] = True
# t = dfs((tx, ty))
# # print(t)
# # print(done)

# # 1回目の
# done = [[False for _ in range(m)] for i in range(m)]
# reset((sx, sy), t)
# done[sx][sy] = False
# done[tx][ty] = True
# que = Deque()
# que.append((tx, ty, t))
# p = dfs((sx, sy))
# # print(p)
# # print(done)


# done = [[False for _ in range(m)] for i in range(m)]
# reset((sx, sy), p)
# done[sx][sy] = True
# done[tx][ty] = False
# # print(done[tx][ty])
# que = Deque()
# que.append((sx, sy, p))
# q = dfs((tx, ty))
# # print(q)


# done = [[False for _ in range(m)] for i in range(m)]
# reset((sx, sy), q)
# done[sx][sy] = False
# done[tx][ty] = True
# que = Deque()
# que.append((tx, ty, q))

# ans = dfs((sx, sy))
# print("".join(ans))

# # print(*ans)


diffx = tx - sx
diffy = ty - sy

ans = []
# 1回目
ans.append("R"*diffx)
ans.append("U"*diffy)
ans.append("L"*diffx)
ans.append("D"*diffy)

# 2回目
ans.append("D")
ans.append("R"*(diffx+1))
ans.append("U"*(diffy+1))
ans.append("L")
ans.append("U")
ans.append("L"*(diffx+1))
ans.append("D"*(diffy+1))
ans.append("R")

print("".join(ans))