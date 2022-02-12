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
"""nの約数を列挙"""
""" 計算量は O(√n)"""
def eratosthenes(n):
    count = [0] * n
    primes = []
    for i in range(2, n):
        if count[i] != 0: continue
        primes.append(i)
        #　iを因数にもつ全ての値に+1する。
        for j in range(i, n, i):
            count[j] += 1
        
    return count, primes

n = int(input())

_, primes = eratosthenes(55555)

ok = []
for i in range(len(primes)):
    s = str(primes[i])
    if s[-1] == "1":
        ok.append(primes[i])


# print(primes, len(primes))
# print(ok)
print(* ok[1:1+n])

# 5637個

