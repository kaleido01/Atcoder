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

inithwv = lambda h, w, v: [[v for _ in range(w)] for _ in range(h)]
inithw = lambda h: [ list(input()) for _ in range(h)]
# initFalse = lambda h, w: [[False for _ in range(w)] for _ in range(h)]
initDp = lambda n:[[] for _ in range(n)]
bit = lambda n, k:((n >> k) & 1) # nのkビット目
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

n, m = mapInt()

pipe = []
pool = init1(n+1)

currentIndex = init0(m)
que = deque()

for i in range(m):
    input()
    pipe.append(listInt())
    top = pipe[-1][0]
    if pool[top] == -1:
        pool[top] = i
    else:
        que.append((pool[top], i))
        
# print(que, pool, pipe)

# if len(que) == 0:
#     print("No")
#     sys.exit()


for i in range(n):
    # print(que, pool, pipe, currentIndex)

    if len(que) == 0:
        print("No")
        sys.exit()
    pipe1, pipe2 = que.popleft()
    currentIndex[pipe1] += 1
    currentIndex[pipe2] += 1
    
    if currentIndex[pipe1] != len(pipe[pipe1]) and currentIndex[pipe2] != len(pipe[pipe2]):
        pass
    elif currentIndex[pipe1] != len(pipe[pipe1]):
        newItem1 = pipe[pipe1][currentIndex[pipe1]]
        if pool[newItem1] != -1:
            que.append((pool[newItem1], pipe1))
        else:
            pool[newItem1] = pipe1
        # if len(que) == 0:
        #     print("No")
        #     sys.exit()
        continue
    elif currentIndex[pipe2] != len(pipe[pipe2]):
        newItem2 = pipe[pipe2][currentIndex[pipe2]]
        if pool[newItem2] != -1:
            que.append((pool[newItem2], pipe2))
        else:
            pool[newItem2] = pipe2
        # if len(que) == 0:
        #     print("No")
        #     sys.exit()
        continue
    else:
        if i == n-1:
            continue
        if len(que) == 0:
            print("No")
            sys.exit()
        continue
    
    newItem1 = pipe[pipe1][currentIndex[pipe1]]
    newItem2 = pipe[pipe2][currentIndex[pipe2]]
    # print(newItem1, newItem2)

    if newItem1 == newItem2:
        que.append((pipe1, pipe2))
        continue
    if pool[newItem1] == -1 and pool[newItem2] == -1:
        pool[newItem2] = pipe2
        pool[newItem1] = pipe1
        continue
    if pool[newItem1] != -1 and pool[newItem2] == -1:
        pool[newItem2] = pipe2
        que.append((pool[newItem1], pipe1))
        continue
    if pool[newItem2] != -1 and pool[newItem1] == -1:
        pool[newItem1] = pipe1
        que.append((pool[newItem2], pipe2))
        continue
    if pool[newItem2] != -1 and pool[newItem1] != -1:
        que.append((pool[newItem1], pipe1))
        que.append((pool[newItem2], pipe2))
    
    

        
print("Yes")