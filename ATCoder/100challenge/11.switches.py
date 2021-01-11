# n, m = map(int, input().split())
# s = []
# for i in range(m):
#   s.append([v for v in list(map(int, input().split()))])
# p= list(map(int, input().split()))
# ans = 0
# # ある電球にたいしてonになっているスイッチの数
# onSwitch = 0
# # 点灯している電球の数
# onLight = 0

# def binary(x):
#   bit = [0] * (30)
#   i=0
#   while (True):
#     bit[i] = x % 2
#     if x // 2 == 0:
#       break
#     x = x //2
#     i +=1
#   return bit
    
# for i in range(2**n):
#   bit = binary(i)
#   # all light bulb check
#   for j in range(m):
#     # check ok light
#       for k in range(s[j][0]):
#         if bit[s[j][k+1]-1] == 1:
#           onSwitch +=1
#       if onSwitch % 2 == p[j]:
#         onLight +=1
#       onSwitch= 0
#   if onLight == m:
#     ans +=1
#   onLight = 0  

# print(ans)
        
        
for i in range(2**2):
  for j in range(2):
    if (i >> j) & 1:
      print(i & 1)
      
  
        
        
        
