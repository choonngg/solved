# ### O(N**3)풀이
# INF = int(1e7)

# N = 11

# use1 = use3 = use4 = None
# min_use = INF

# for a in range(N//1 + 1):
#     for b in range(N//3 + 1):
#         for c in range(N//4 + 1):
#             if a + 3*b + 4*c == N:
#                 if a + b + c <= min_use:
#                     min_use = a + b + c
#                     use1 = a
#                     use3 = b
#                     use4 = c

# print(f"1원은 {use1}개 사용 / 3원은 {use3}개 사용 / 4원은 {use4}개 사용")



### O(N) 풀이
##  a를 최대한 안쓰는 방식으로 감 -> 결국엔 b와 c만 정하면 됨
##  b와 c중 하나만 정하면 나머지가 정해지기 때문에 O(N)풀이가 가능
MAX = int(1e7)
N = 11

min_use = MAX
use1 = use3 = use4 = None

for c in range(N//4 + 1):
    b = (N-4*c) // 3
    a = (N-4*c) % 3
    if a + b + c < min_use:
        min_use = a + b + c
        use1 = a
        use3 = b
        use4 = c

print(f"1원은 {use1}개 사용 / 3원은 {use3}개 사용 / 4원은 {use4}개 사용")