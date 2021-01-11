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

n, k = mapInt()

a  = listInt()


dp = [[0 for _ in range(k+10)] for _ in range(n+10)]
dp[0][0] =1
for i in range(1,n+1):
  s = [0] * (k+5)
  s[0] = 0
  for j in range(k+1):
    s[j+1] = s[j] + dp[i-1][j] % MOD
  # print(s)
  for j in range(k+1):
    # print(i,j)
    dp[i][j] = s[j+1] - s[max(0, j - a[i-1])] % MOD
    
    
    
print(dp[n][k] % MOD)