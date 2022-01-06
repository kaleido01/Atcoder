"""有向グラフにおいて 「お互いに行き来できる ⟺ 同じグループ」を満たすように頂点をグループ分け"""
"""適当な頂点から深さ優先探索を行う，その際各頂点 vv に対して頂点 vv から進めなくなった順番 t(v)t(v) を格納する。"""
"""グラフの矢印を全て逆向きにしたものに対して深さ優先探索を行う。その際 t(v)t(v) が大きい頂点からスタートする。行き止まったところまでを一つの連結成分とする。"""



n, m = mapInt()

e1 = [[] for _ in range(n)]
e2 = [[] for _ in range(n)]

for i in range(m):
  a, b  = mapInt()
  a, b = a-1, b-1
  
  e1[a].append(b)
  e2[b].append(a)



f = [-1] * n
done = [False] * n
# 帰りがけで順番を記録
def dfs1(start, pos = 0):
  edges = e1[start]
  
  # hasNext = False
  for edge in edges:
    if done[edge]: continue
    done[edge] = True
    # hasNext = True
    pos = dfs1(edge, pos)
  # if not hasNext:
  f[pos] = start
  pos += 1
  return pos


groups = []
done1 = [False] * n
def dfs2(start, group = []):
  edges = e2[start]
  group.append(start)

  for edge in edges:
    if done1[edge]: continue
    done1[edge] = True
    group = dfs2(edge, group)
  return group

pos = 0
#頂点を辿る順を記録する
for i in range(n):
  if done[i]: continue
  done[i] = True
  
  pos = dfs1(i, pos)


# グループ分け
f.reverse()
for i in f:
  if done1[i]: continue
  done1[i] = True
  
  group = dfs2(i, [])
  groups.append(group)


# print(f)
# print(groups)


ans = 0
for group in groups:
  # print(uf.size(i))
  x = len(group)
  ans += x * (x-1) // 2
  # uf.parents[2]
# for i in range(n):
# print(ans)
print(ans)