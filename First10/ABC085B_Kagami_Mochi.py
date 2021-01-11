a = int(input())

b = []
for i in range(a):
    b.append(int(input()))
b.sort()

count = 1
for i in range(a):
    if i == 0:
        continue
    if b[i] > b[i-1]:
        count += 1
print(count)

# c[] = 0
# for v in b:
#     c[v] += 1

# num = 0
# for v in c:
#     if v > 0:
#         num += 0
