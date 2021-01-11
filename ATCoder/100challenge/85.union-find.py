import sys

sys.setrecursionlimit(10 ** 7)

n,q = map(int, input().split())

tree = [i for i in range(n)]

def find(x):
  par = tree[x]
  if par == x :
    return x
  v = find(par)
  tree[x] = v
  return v
  
    
  
def unite(x,y):
  rx = find(x)
  ry = find(y)

  if rx == ry:
    return
  else:

    tree[ry] = rx


  
def same(x, y):
  rx = find(x)
  ry = find(y)
  return rx == ry

for i in range(q):
  s, t, u = map(int, input().split())
  
  if s==0:
    unite(t,u)
  else:
    ans = same(t,u)
    if ans :
      print("Yes")
    else:
      print("No")
