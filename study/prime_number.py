import math

n = 100
prime_number_count = 0

## O(N**2)
## 브루트포스 알고리즘 풀이
# for i in range(1, n+1):
#     if i == 1: continue
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False

#     if is_prime:
#        prime_number_count += 1 


## O(Nlog(logN)) ~= O(N)
## 에라토스테네스의 체 알고리즘 풀이
is_prime = [True for _ in range(n+1)]
is_prime[0] = False; is_prime[1] = False
for i in range(1, int(math.sqrt(n))+1):
    if not is_prime[i]: continue
    for j in range(2*i, n+1, i):
        is_prime[j] = False

for p in is_prime:
    prime_number_count += p

print(prime_number_count)