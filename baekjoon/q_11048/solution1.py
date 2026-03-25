N, M = map(int, input().split())
miro = [[0 for _ in range(M)] for _ in range(N)]
for i in range(0, N):
    miro[i] = list(map(int, input().split()))

# 초기값 설정
dp_table = [[0 for _ in range(M)] for _ in range(N)]
dp_table[0][0] = miro[0][0]
for i in range(1, M):
    dp_table[0][i] = dp_table[0][i-1] + miro[0][i]
for i in range(1, N):
    dp_table[i][0] = dp_table[i-1][0] + miro[i][0]


# 수식
for i in range(1, N):
    for j in range(1, M):
        dp_table[i][j] = max(dp_table[i][j-1], dp_table[i-1][j], dp_table[i-1][j-1]) + miro[i][j]

print(dp_table[N-1][M-1])