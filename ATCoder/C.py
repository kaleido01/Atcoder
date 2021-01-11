import itertools
n, k = map(int, input().split())

# map = [[0]* n for _ in range(n) ]
# for i in range(n):
#   map.append([ v for v in list(map(int, input().split()))])

map=[list(map(int,input().split())) for _ in range(n)]

p = list(itertools.permutations([i for i in range (1,n)],n-1))

count = 0
for x in p:
  sum = 0
  last = 0
  for i in x:
    sum += map[last][i]
    last = i
  sum += map[i][0]
  if sum == k:
    count += 1

print(count)