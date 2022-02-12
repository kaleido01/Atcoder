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

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter


s = input()
n = len(s)
ans = 500
before = s[0]

def setHand(num):
  return 1 <= int(num) <= 5


# left = 1 right = 0
hand = setHand(s[0])




for i in range(1, n):
  if s[i] == before:
    ans += 301
  elif setHand(s[i]) == hand:
    ans += 210
    before = s[i]
  else:
    ans +=100
    hand = setHand(s[i])
    before = s[i]
    
print(ans)
  