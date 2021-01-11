n, k = map(int, input().split())
y = list(map(int, input().split()))


dp = [float("inf")] * (10 ** 5 + 100)
# print(y)


dp[0] = 0
for i in range(0, n):
    for j in range(1, k+1):
        if j+i <= n-1:
            dp[i+j] = min(dp[i+j], dp[i] + abs(y[i] - y[i+j]))
print(dp[n-1])
