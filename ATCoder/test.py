def isOk(index, key, array):
  return array[index]<=key
def lower_search(v,array):
  ng = -1
  ok = len(array)
  
  while(abs(ok - ng) >1):
    # middle = left  + (left - right) //2
    middle = (ok + ng)//2
    if isOk(middle,v,array):
      ok = middle
    else:
      ng = middle
  return ok

def upper_search(v,array):
  ok = -1
  ng = len(array)
  
  while(abs(ok-ng)>1):
    # middle = left  + (left - right) //2
    middle = (ok + ng)//2
    if isOk(middle,v,array):
      ok = middle
    else:
      ng = middle
  print(ok,ng)
  return ok

a= [[],[1,2],3,4]
# print(a[-1])
print(1<<10)

# print()



relation = [ {} for _ in range(4)]

relation[1][2] = 3
print(relation)

for key, value in relation[0].items():
  print(key,value)