# -*- coding: utf-8 -*-
from curses import nocbreak
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect, statistics
from collections import Counter, defaultdict, deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
mapInt = lambda: map(int, input().split())
listInt = lambda: list(map(int, input().split()))

init0 = lambda n: [0 for _ in range(n)]
inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h, w: [ listInt() for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]

YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1
from operator import itemgetter

s = input()

x = s[:2]
y = s[2:]
# print(x, y)

def tuki(x):
  return 1 <= int(x) <= 12

def year(x):
  return not(x[0] == 0 and x[1] == 0)

if tuki(x) and year(y) and year(x) and tuki(y):
  print("AMBIGUOUS")
  sys.exit()
if year(x) and tuki(y):
  print("YYMM")
  sys.exit()
if year(y) and tuki(x):
  print("MMYY")
  sys.exit()
  
print("NA")

    