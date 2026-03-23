# 브루트포스 풀이 
# -> 시간초과지만 일단 풀었음...
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = int(1e7)
for per_A in permutations(A, len(A)):
    sum = 0
    for i in range(N):
        sum += per_A[i] * B[i]
    if sum < S:
        S = sum

print(S)