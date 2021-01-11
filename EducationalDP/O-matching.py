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
initinthw = lambda h: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter


n = int(input())


a = initinthw(n)


# 計算量( 2^n n^2)
# dp = [[0 for i in range( 1 << n)] for i in range(n+1)]

# dp[0][0] = 1

# for i in range(n+1):
#   for s in range(1 << n):
#     # count = 0
#     bin(n).count("1")
#     for k in range(n):
#       if bit(s, k) and a[i-1][k]:
#         dp[i][s] = (dp[i][s] + dp[i-1][(1 << k) ^ s]) % MOD
    
    


dp = [0 for i in range(1<<n)]
dp[0] =1

# sが決まるとペアを組んだ男女の数が決まる
for s in range(1 << n):
  pair = bin(s).count("1")
  for k in range(n):
    if bit(s, k) and a[pair-1][k]:
      dp[s] = (dp[s] + dp[(1 << k) ^ s]) % MOD
    

print(dp)
print(dp[s] % MOD)
    
    
    


