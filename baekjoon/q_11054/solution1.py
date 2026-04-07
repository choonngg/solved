N = int(input())
S = list(map(int, input().split()))

increase = [1] * N
decrease = [1] * N
dp = [0] * N

for i in range(0, N):
    for j in range(i):
        if S[i] > S[j] :
            increase[i] = max(increase[i], increase[j]+1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if S[i] > S[j] :
            decrease[i] = max(decrease[i], decrease[j]+1)

for i in range(N):
    dp[i] = increase[i] + decrease[i] - 1

print(max(dp))