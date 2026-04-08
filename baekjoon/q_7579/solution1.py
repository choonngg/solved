N, M = map(int, input().split())
m = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(10001)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(10001):
        dp[i][j] = dp[i-1][j]
        if c[i] == j:
            dp[i][j] = max(dp[i-1][j], m[i])
        if j - c[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j - c[i]] + m[i])

ans = 0
for i in range(10001):
    if dp[N][i] >= M:
        ans = i
        break
print(ans)