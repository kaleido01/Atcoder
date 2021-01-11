n,m= map(int, input().split())

p=list(map(int,input().split()))

tree = [i for i in range (n+1)]

def find(x):
  par = tree[x]
  if par == x:
    return x 
  else:
    tree[x] = find(tree[x]) #経路圧縮
    return tree[x]

def unite(x, y):
  rx = find(x)
  ry = find(y)
  
  if rx == ry:
    return
  tree[rx] = ry
  
def same(x,y):
  rx = find(x)
  ry = find(y)
  
  return rx == ry

for i in range(m):
  x, y = map(int, input().split())
  unite(x,y)

ans = 0
for i in range(0,n):
  dest = p[i]
  if same(i+1,dest):
    ans +=1

print(ans)