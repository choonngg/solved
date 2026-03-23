N = int(input())
N = 1000 - N
min = 0

for i in [500, 100, 50, 10, 5, 1]:
    min += (N // i)
    N = N % i

print(min)