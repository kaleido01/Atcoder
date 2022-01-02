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

# h, w = mapInt()
n, k = mapInt()

a = listInt()

used = {}

right = 0
ans = 0

for left in range(n):
    while (right < n and len(used.keys()) <= k):
        # 実際に right を 1 進める */
        # ex: sum += a[right];
        
        if a[right] in used.keys():
          used[a[right]] += 1
        else:
          if len(used.keys()) == k:
            break
          else:
            used[a[right]] = 1
        right += 1

    # break した状態で right は条件を満たす最大なので、何かする */
    # ex: res += (right - left);
    # if right == n:
    #   ans = max(ans, right - left)
    # else:
    #   ans = max(ans, right - left)
    ans = max(ans, right - left)
    


    # left をインクリメントする準備 */
    # print(left, right, used)
    if used[a[left]] == 1:
      del used[a[left]]
    else:
      used[a[left]] -= 1
    # ex: if (right == left) ++right;
    # ex: else sum -= a[left];


print(ans)