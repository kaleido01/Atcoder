# -*- coding: utf-8 -*-
from itertools import combinations, permutations, combinations_with_replacement
from operator import itemgetter
import sys

sys.setrecursionlimit(10**9)
INF = 10**18
MOD = 10**9+7
def input(): return sys.stdin.readline().rstrip()
def mapInt(): return map(int, input().split())
def listInt(): return list(map(int, input().split()))


def init0(n): return [0 for _ in range(n)]
def inithwv(h, w, v): return [[v for _ in range(w)] for _ in range(h)]


def inithw(h): return [list(input())for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
def initDp(n): return [[] for _ in range(n)]


def YesNo(b): return bool([print('Yes')] if b else print('No'))
def YESNO(b): return bool([print('YES')] if b else print('NO'))


def int1(x): return int(x)-1


s = input()
x = int(input())

count = []


def isOk(index, key):
    return count[index][0] >= key


def binary_search(v, right):
    left = -1
    right -= 1
    while(right - left > 1):
        # middle = left + (left - right)//2
        middle = (left + right)//2
        if isOk(middle, v):
            right = middle
        else:
            left = middle
    return right


def solve(ok, index, v):
    # indexの操作が文字だった場合その文字を追加して条件を満たしているはずなのでその文字が答え
    if index + 1 == count[index][0]:
        print(count[index][1])
        sys.exit()

    if v % ok == 0:
        v = count[index-1][0]
    else:
        v %= ok

    # ２分探索で該当の値に近いところを求める。
    # この場合 xxxxxoooooooになるぎりぎりのoを求める
    nIndex = binary_search(v, index)
    if v == count[nIndex][0]:
      print(count[nIndex][1])
      sys.exit()

    solve(count[nIndex-1][0], nIndex, v)


for i in range(len(s)):
    if ord("a") <= ord(s[i]) <= ord("z"):
      if i != 0:
        count.append([count[i-1][0] + 1,s[i]])
      else:
        count.append([1,s[i]])
    if 1 <= ord(s[i]) - ord("0") <= 9:
      a, string = count[i-1] if i != 0 else (0,"")
      count.append([a * (int(s[i])+1),string])
    # print(count[i])
    if count[i][0] == x:
      # print(count[i][0])
      print(count[i][1])
      sys.exit()
    if count[i][0] > x:
      solve(count[i-1][0], i, x)

    
