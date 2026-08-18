N = 6
f = [0] * (N+1)

f[1] = 1
f[2] = 2
f[3] = 1
f[4] = 1

for i in range(5, N+1):
    f[i] = min(f[i-1], f[i-3], f[i-4]) + 1

print(f[N])