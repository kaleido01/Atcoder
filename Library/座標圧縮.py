# coding: utf-8
import itertools

# 座標圧縮したい数列
A = [8, 100, 33, 33, 33, 12, 6, 1211]

# 集合型にすることで重複を除去し、
# 小さい順にソートする
B = sorted(set(A))

# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v: i for i, v in enumerate(B) }

# 答え
x = map(lambda v: D[v], A)
print(x)
print(list(x))


A = [[8,100], [33, 33], [33, 12], [6, 1211]]
B = sorted(set(list(itertools.chain.from_iterable(A))))

D = { v: i for i, v in enumerate(B) }

newArray = []
def f(v):
  print(v)
  x = D[v[0]]
  y = D[v[1]]
  # newArray.append((x,y))
  return [x, y]
x = map(f, A)
print(B,D, list(x))