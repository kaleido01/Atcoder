# -*- coding: utf-8 -*-
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(3*10**5+10)
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


t = listInt()
s = [0] * (n+1)

for i in range(n):
  s[i+1] = s[i] + t[i]
end = s[n]
v = listInt()


maxV = 50
dp = [ [ -1 for i in range(maxV+1)] for _ in range(end+1)]

dp[0][0] = 0

now = 0
# print(s)
def currentMax(time):
  index = bisect.bisect_left(s, time)
  if time < 63:
    print(s, time, index, v[index-1])
  return v[index-1]
  
# n個目
for i in range(end):
  for j in range(maxV):
    if dp[i][j] == -1: continue
    if j > currentMax(i+1):
      dp[i][j] = -1
      continue
    if currentMax(i+1) >= j+1:
      dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + j + 0.5)
    else:
      pass
      # dp[i][j] = -1
      # continue
    if j-1 >= 0:
      dp[i+1][j-1] = max(dp[i+1][j-1], dp[i][j] + j - 0.5)
    dp[i+1][j] = max(dp[i+1][j], dp[i][j] + j)

# print(dp)
print(dp[end][0])


