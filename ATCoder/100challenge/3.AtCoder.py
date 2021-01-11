# a, b = map(int, input().split())
# if (a*b) % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# N = input()
# a = int(input())
# b = int(input())
# c = int(input())
# x = int(input())


# count = 0

# num = x / a
# x -= num * 500

n, a, b = map(int, input().split())

count = 0
for i in range(n+1):
    if i == 0:
        continue
    x = list(map(int, list(str(i))))
    sum = 0
    for v in x:
        sum += v
    if a <= sum <= b:
        count += i


print(count)

print(list("aaaa"))
