n, y = map(int, input().split())


isExist = False


# def check(v):
#     left = 0
#     right = n

#     while(left <= right):
#         print("aa")
#         middle = left + right // 2
#         if v == middle:
#             return True
#         elif v < middle:
#             right = middle - 1
#         else:
#             left = middle + 1
#     return False


for i in range(n+1):
    for j in range(n+1):
        res = (y - i * 10000 - j * 5000) // 1000
        if i + j + res == n and res >= 0:
            print(i, j, res)
            isExist = True
            break
    if isExist:
        break

       #     break
       # if check(res) and i + j + res == n:
       #     print("%d %d %d", i, j, res)
       #     false = True
       #     break

if isExist == False:
    print("-1 -1 -1")
