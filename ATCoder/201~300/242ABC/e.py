# -*- coding: utf-8 -*-
import sys, getpass, string
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(3*10**5+10)
INF=10**18
MOD=998244353 # 998244353
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


al = string.ascii_lowercase

ans=[]
def solve(p, s):
  dp = [ [ 0 for i in range(2)] for i in range(p // 2 + 1)]
  dp[0][0] = 1
  
  
  for i in range(p // 2):
    # isSame-> isSame
    # 対象の2文字のうち
    dp[i+1][0] += dp[i][0]
    
    
    # isSame-> isLower
    # 自分の文字より下ならOK
    rest = ord(s[i]) - ord('A')
    dp[i+1][1] += rest * dp[i][0]
    
    # isLower-> isLower
    # 後ろはなんでも良い
    dp[i+1][1] += 26 * dp[i][1]
    
    dp[i+1][1] %= MOD
    dp[i+1][0] %= MOD
  if p % 2 == 1:
    x = 0
    # isLowerの場合はなんでも良い
    x += 26 * dp[p//2][1]
    # isSameの場合はそれ以下なので
    rest = ord(s[p//2]) - ord('A')
    x += rest * dp[p//2][0]
    
    # 真ん中まで一致している場合一つ増えるため

    former = s[:p//2]
    former = former[::-1]
    back = s[p//2+1:]
    if former <= back:
      x +=1
    x %= MOD
    # print("fssss", former, back)
    
    ans.append(x)
    # print(dp)
  else:
    # print(dp)
    former = s[: p//2]
    former = former[::-1]
    back = s[p//2:]
    if former <= back:
      p = sum(dp[p//2])
      p %= MOD
      ans.append(p)
    else:
      p = sum(dp[p//2])-1
      p %= MOD
      ans.append(p)
  
for i in range(n):
  p = int(input())
  s = input()
  solve(p, s)
print(*ans)