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
# YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
#組み合わせ総数
def combinations_count(n, r):
  if n - r < 0: return 0
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# h, w = mapInt()
n = int(input())

dic = [0] * 100
for i in range(2, n+1):
  a = factorization(i)
  
  for v, cnt in a:
      dic[v] +=cnt
# print(dic)

# 2, 4, 4
c2 = 0
c4 = 0
for value in dic:
  if value >= 4:
    c4 +=1
  elif 2<= value < 4:
    c2 +=1

ans = 0

ans += combinations_count(c4, 2) * (c4-2) + combinations_count((c4), 2) * c2
# print(ans)

# 2, 24
c2 = 0
c24 = 0
for value in dic:
  if value >= 24:
    c24 +=1
  elif 2<= value < 24:
    c2 +=1

ans += combinations_count(c24, 1) *(c24-1) + c24 * c2
# print(ans)

# 4, 14
c4 = 0
c14 = 0
for value in dic:
  if value >= 14:
    c14 +=1
  elif 4<= value < 14:
    c4 +=1

ans += combinations_count(c14, 1) * (c14-1) + c14 * c4
# print(c4, c14, ans)
# 74
c74 = 0
for value in dic:
  if value >= 74:
    c74 +=1
ans += c74


# ans = 0
# # 3 25
# for i in range(100):
#   for j in range(100):
#     if i != j and dic[i] >= 2 and dic[j] >= 24:
#       print(dic[i], dic[j])
#       ans+=1
# print("ans1", ans)
      
# # 4 14
# for i in range(100):
#   for j in range(100):
#     if i != j and dic[i] >= 4 and dic[j] >= 14:
#       print(dic[i], dic[j])
#       ans+=1
# print("ans2", ans)

# # 3, 5, 5
# for i in range(100):
#   for j in range(100):
#     for k in range(j+1, 100):
#       if i != j and j != k and i != k and dic[i] >= 2 and dic[j] >= 4 and dic[k] >= 4:
#         print(dic[i], dic[j], dic[k])
#         ans+=1
# print("ans3", ans)

# # 75
# for i in range(100):
#       if dic[i] >= 74 :
#         ans+=1


print(ans)