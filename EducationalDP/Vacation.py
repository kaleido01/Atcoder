n = int(input())

a = []
b = []
c = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x[1])
    b.append(x[2])
    c.append(x[3])


dp = [3][0]
for v in range(n + 2):
