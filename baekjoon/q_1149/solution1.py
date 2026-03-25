N = int(input())
rgb = [[0, 0, 0]]
for _ in range(N):
    rgb.append(list(map(int, input().split())))

dp_table = [[0, 0, 0] for _ in range(N+1)]
for i in range(3):
    dp_table[1][i] = rgb[1][i]

for i in range(2, N+1):
    dp_table[i][0] = min(dp_table[i-1][1], dp_table[i-1][2]) + rgb[i][0]
    dp_table[i][1] = min(dp_table[i-1][0], dp_table[i-1][2]) + rgb[i][1]
    dp_table[i][2] = min(dp_table[i-1][0], dp_table[i-1][1]) + rgb[i][2]

print(min(dp_table[N][0], dp_table[N][1], dp_table[N][2]))