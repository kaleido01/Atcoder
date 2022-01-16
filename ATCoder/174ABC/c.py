# -*- coding: utf-8 -*-
from email.mime import base
import sys
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

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



k = int(input())

ai = 7
ai %= k
if ai == 0:
    print(1)
    sys.exit()
cnt = [0] * k
cnt[ai] += 1
for i in range(1, k):
    ai = (ai * 10 + 7) % k
    # print(ai)
    if ai == 0:
        print(i+1)
        sys.exit()
print(-1)

    
        
    
