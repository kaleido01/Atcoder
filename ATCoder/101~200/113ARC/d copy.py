# -*- coding: utf-8 -*-
from re import L
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
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
# YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n = int(input())
s = list(input())
# s += s
# print(s)
# print(ans)
def check(index):
  if ans[index] == "S" and s[index] == "o":
    if ans[index-1] == 'S':
      ans.append("S")
    else:
      ans.append("W")
  elif ans[index] == "S" and s[index] == "x":
    if ans[index-1] == 'S':
      ans.append("W")
    else:
      ans.append("S")
  elif ans[index] == "W" and s[index] == "o":
    if ans[index-1] == 'S':
      ans.append("W")
    else:
      ans.append("S")
  else:
    if ans[index-1] == 'S':
      ans.append("S")
    else:
      ans.append("W")

def ok():
  if ans[0] == "S" and s[0] == "o":
    if ans[-1] == 'S':
      return ans[1] == "S"
    else:
      ans.append("W")
  elif ans[0] == "S" and s[0] == "x":
    if ans[-1] == 'S':
      ans.append("W")
    else:
      ans.append("S")
  elif ans[0] == "W" and s[0] == "o":
    if ans[-1] == 'S':
      ans.append("W")
    else:
      ans.append("S")
  else:
    if ans[-1] == 'S':
      ans.append("S")
    else:
      ans.append("W")
ans = []
  
for i in range(1,4):
  ans = []
  # if i == 0:
  #   ans.append("S")
    # ans.append("S")
  if i == 1:
    ans.append("S")
    ans.append("W")
  if i == 2:
    ans.append("W")
    ans.append("S")
  if i == 3:
    ans.append("W")
    ans.append("W")
  for j in range(1, n):
    check(j)
  x = "".join(ans)
  print(ans)
  if ans[0] == ans[n] and ok():
    print(x[:n])
    exit()
print(-1)

    
    