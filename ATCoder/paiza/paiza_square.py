n = int(input())

height = [[] for _ in range(10)]

for _ in range(n):
  p = list(input().split())
  operand = p[0]
  x= int(p[1])
  y= int(p[2])
  a = int(p[3])
  # yet left
  status = "yet"
  for j in range(y,y+a):
    for d in height[j]:
      left = 0
      for sx,ex in d.items():
        if operand == "+":
          if x > sx:
            status = "left"
          if status == "left":
            if x+a < ex:
              d[x] = ex
            else:
              del d[x]
        else:
          print("-")
        left = ex
    if status == "yet":
      height[j].append({x:x+a})
      
  
print(height) 