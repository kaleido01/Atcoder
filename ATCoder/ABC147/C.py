N = int(input())

# i番目の配列にi番目の証言が全て格納
items = [[] for _ in range(N)]

for i in range(N):
  a = int(input())
  for j in range(a):
    # x番目は正直( y == 1 ) or 不親切 ( y == 0)
    x, y = map(int, input().split())
    x -= 1
    items[i].append((x,y))
    
# 全探索

maxCount = 0
for i in range(2 ** N):
  count = 0
  isOK = True
  #矛盾がないか確認
  for j in range(N):
    if ((i>>j) & 1):# j番目が正直者のとき
      count += 1
      if len(items[j]) == 0:
        continue
      # 正直者の証言を確認して正しいかを確認する
      for item in items[j]:
        x,y = item

        if i >> x & 1 == True and y == 0:
 
          isOK = False
        if i >> x & 1 == False and y == 1:
          # print("ggg")
          isOK = False

  if isOK:
    maxCount = max(maxCount, count)

print(maxCount)
    
      