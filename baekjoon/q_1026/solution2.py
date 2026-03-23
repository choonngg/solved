# 그리디 풀이
# -> 그냥 ㅈ까고 B도 재배치 하는 경우
# -> 우선순위 : A의 최소값, B의 최대값

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse = True)
S = 0
for i in range(N):
    S += A[i] * B[i]
# for a, b in zip(A, B):
#     S += a * b

print(S)