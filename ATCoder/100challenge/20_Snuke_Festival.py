
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
# b.sort()
c.sort()

def isOk(index, key, array,down):
  if down:
    return array[index]>=key
  else:
    return array[index] <= key
  
def lower_search(v,array):
  ng = -1
  ok = len(array)
  
  while(abs(ok - ng) >1):
    # middle = left  + (left - right) //2
    middle = (ok + ng)//2
    if isOk(middle,v,array,True):
      ok = middle
    else:
      ng = middle
  return ok

def upper_search(v,array):
  ok = -1
  ng = len(array)
  
  while(abs(ok - ng) >1):
    # middle = left  + (left - right) //2
    middle = (ok + ng)//2
    if isOk(middle,v,array,False):
      ok = middle
    else:
      ng = middle
  return ok

sum = 0
for v in b:
  minA = lower_search(v,a)
  maxC = upper_search(v,c)
  
  okA=0
  okC=0
  if minA == -1:
    okA=0
  elif minA ==len(a):
    okA = len(a)
  else:
    okA = minA
    
  if maxC == -1:
    okC = len(c)
  elif maxC ==len(c):
    okC = 0
  else:
    okC= len(c) - maxC-1
    
  sum += okA*okC
  
print(sum)