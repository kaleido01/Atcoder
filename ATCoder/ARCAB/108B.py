# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD= 998244353 # 998244353
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
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n = int(input())

s = input()



# ans = 0
# i = 0

# def ok(pos):
#   left = pos
#   right = pos
#   cnt = 0
#   while(left >= 2 and right < n-5):
#     if s[right + 3] == "f" and s[right + 4] == "o" and s[right + 5] == "x":
#       right += 3
#       cnt += 1
#       # print("1")
#     elif s[left - 1] == "f" and s[right + 3] == "o" and s[right + 4] == "x" :
#       right += 2
#       left  -= 1
#       cnt +=1
#       # print("2")
#     elif s[left - 2] == "f" and s[left - 1] == "o" and s[right + 3] == "x" :
#       right += 1
#       left  -= 2
#       cnt +=1
#       # print("3")
#     else:
#       return (right, cnt)
#   return (right, cnt)
  

# while(i < n - 2):
#   # foxを探す
#   cnt = 0
#   while(i < n - 2 and not (s[i] == "f" and s[i+1] == "o" and s[i+2] == "x")):
#     i += 1
  
#   if i < n - 2 and s[i] == "f" and s[i+1] == "o" and s[i+2] == "x": 
#     ans += 1
#     pos, cnt = ok(i)
#     print(pos, cnt)
#     i = pos+1
#   #両端でからFOXになる組み合わせを探す

#   ans += cnt
  

# print(n - 3 * ans)
# # print(ans)




def dfs(start, cnt):
  if s[start] == "f" and s[start+1] == "o" and s[start+2] == "x":
    return (start+3, cnt+1)
  if s[start] == "f" and s[start+1] == "f":
    start, cnt = dfs(start+1, cnt)
    if s[start] == 
  if s[start] == "o" and s[start+1] == "f":
    dfs(start+1, cnt)
  