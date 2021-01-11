n, q = map(int,input().split())

c = list(map(int, input().split()))

par = [i for i in range(n+1)]
cnt = [i for i in range(n+1)]
relation = [ {} for _ in range(n+1)]


for i in range(len(c)):
  key = c[i]
  relation[i+1][key] = 1
  
  
def find(x):
  if x == par[x]:
    return x
  else:
    par[x] = find(par[x])
    return par[x]

def unite(x, y):
  rx = find(x)
  ry = find(y)
  
  if rx == ry:
    return
  else:
    if cnt[rx] > cnt[ry]:
      rx, ry = ry, rx
    par[rx] = ry
    cnt[ry] += cnt[rx]
    #グループメンバーのクラス分け更新
    # for i in range(n):
    #   relation[ry][i+1] += relation[rx][i+1]
    for key, value in relation[rx].items():
      if key in relation[ry]:
        relation[ry][key] += value
      else:
        relation[ry][key] = value
      
    
def same(x,y):
  return find(x) == find(y)

  
for i in range(q):
  s,t,u = map(int, input().split())
  if s == 1:
    unite(t,u)
  else:
    if u in relation[find(t)]:
      print(relation[find(t)][u])
    else:
      print(0)
  