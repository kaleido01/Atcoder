# -*- coding: utf-8 -*-
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque




minHeap = []
heapq.heappush(minHeap,(0, start))

while(minHeap):
  # 先頭のキューを取り出す。取り出したキューは確定地点である。
  cost , currentNode = heapq.heappop(minHeap)
  
  # すでにコストが現在の最小を上回っている場合はスキップ
  if cost > ans[currentNode]:
    continue
  
  # その頂点から辿れるノード先のコストを計算して、最小値を更新する。
  for node in nodes[currentNode]:
    node, weight = node
    if ans[node] > weight + cost:
      ans[node] = weight + ans[currentNode]
      heapq.heappush(minHeap, (ans[node], node))