# -*- coding: utf-8 -*-
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
intInput = lambda: int(input())
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

n,k  = mapInt()

if n == 0:
  print(0)
  sys.exit()

def base_10(num_n,n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

# def base_n(num_10,n):
#     str_n = ''
#     while num_10:
#         if num_10%n>=10:
#             return -1
#         str_n += str(num_10%n)
#         num_10 //= n
#     return int(str_n[::-1])


def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        addNum = num_10%n
        if addNum == 8:
          str_n += str(5)
        else:
          str_n += str(addNum)
        num_10 //= n
    return int(str_n[::-1])


next = n
for i in range(k):
  n10 = base_10(next, 8)
  n8 = base_n(n10, 9)
  next = n8

print(next)

