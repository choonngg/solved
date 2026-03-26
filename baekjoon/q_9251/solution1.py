S1 = input()
S2 = input()

N = len(S1)
M = len(S2)

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        if S1[j-1] == S2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[M][N])