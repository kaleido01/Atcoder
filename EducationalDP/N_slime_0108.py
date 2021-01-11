# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
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
from operator import itemgetter


n = int(input())

a = listInt()

dp = [ [ INF for i in range(n+1)] for i in range(n+1)]


s = [0] * (n+1)

for i in range(n):
  s[i+1] = s[i] + a[i]

def dig(i,j):
  if dp[i][j] != INF:
    return dp[i][j]
  
  if j - i == 0 :
    return 0
  
  # if j ^ i == 1:
  #   dp[i][j] = a[i] + a[j]
  #   return dp[i][j]
  
  minV = INF
  for k in range(i, j):
    minV = min(minV ,dig(i,k) + dig(k+1, j))
    
  # print(minV)
  dp[i][j] = minV + s[j] - s[i-1]
  
  # print(dp)
  return dp[i][j]


dig(1,n)
# print(s)
print(dp[1][n])