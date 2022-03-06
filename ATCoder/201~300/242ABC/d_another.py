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

s = input()
Q = int(input())

q = []

for i in range(Q):
  t, k = mapInt()
  q.append((t, k))



ans = []

# isFirstは手前 つまりbit0 
def next(s, isFirst):
  if s == "A":
    if isFirst:
      return "B"
    else:
      return "C"

  if s == "B":
    if isFirst:
      return "C"
    else:
      return "A"
  if s == "C":
    if isFirst:
      return "A"
    else:
      return "B"
    

def skip(x, rest):
  if x == "A":
    if rest == 0:
      return "A"
    if rest == 1:
      return "B"
    if rest == 2:
      return "C"
  if x == "B":
    if rest == 0:
      return "B"
    if rest == 1:
      return "C"
    if rest == 2:
      return "A"
  if x == "C":
    if rest == 0:
      return "C"
    if rest == 1:
      return "A"
    if rest == 2:
      return "B"
    


def solve(temp, startS, al):
  now = startS
  cnt = 0
  if temp == 1:
    alt = (al - cnt) % 3
    # print(now, alt, cnt)
    # 残りこの回数分文字を回す必要がある
    p = skip(now, alt)
    return p
  while(temp != 0):
      if temp == 1:
        now = next(now, True)
        # cnt += 1
        break
      now = next(now, temp % 2 == 0)
      temp //= 2
      cnt +=1
  # この段階でcnt回の分裂で欲しいポジションに到着
  if t > cnt:
    alt = (al - cnt) % 3
    # print(now, alt, cnt)
    # 残りこの回数分文字を回す必要がある
    p = skip(now, alt)
    return p
  else:
    return now


for i in range(Q):
  t, k = q[i]
  if t == 0:
    ans.append(s[k-1])
  if k == 1:
    
    ans.append()
  # 最初の文字の中に答えがある
  if t > 60:
    k -= 1
    ans.append(solve(k, s[0], t))
  else:
    po = 2 ** t
    temp = 1
    # print("po", po)
    while temp * po < k:
      temp +=1
    ans.append(solve(k - (temp-1) * po, s[temp-1], t))
      

print(*ans)