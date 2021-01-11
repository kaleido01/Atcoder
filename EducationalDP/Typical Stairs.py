n, m = map(int, input().split())

b = [False] * (10 ** 5 + 100)
for i in range(m):
    b[(int(input()))] = True


dp = [0] * (10 ** 5 + 100)
dp[0] = 1
for i in range(1, n+1):
    if i == 1:
        if not b[i]:
            dp[i] += 1
    if i > 1:
        if not b[i-1] and not b[i-2]:
            dp[i] = dp[i-1] + dp[i-2]
        if b[i-1] and not b[i-2]:
            dp[i] = dp[i-2]
        if not b[i-1] and b[i-2]:
            dp[i] = dp[i-1]
print(dp[n] % 1000000007)
