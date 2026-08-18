T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))

    dp = [([0] * (N+1)) for _ in range(N+1)]

    for i in range(1, N+1):
        getApple = []
        able = True
        for j in range(i, N+1):
            if not able:
                dp[i][j] = dp[i][j - 1]
                continue
            if B[j] in getApple:
                able = False
                dp[i][j] = dp[i][j - 1]
                continue

            getApple.append(B[j])
            dp[i][j] = dp[i][j - 1] + A[j]

    mx = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            mx = max(mx, dp[i][j])

    print(f"#{test_case} {mx}")
