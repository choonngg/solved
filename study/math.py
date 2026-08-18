from math import sqrt

## 약수
def get_divisors(n):
    s = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return s


## 소수
def is_prime(n):
    return (len(get_divisors(n)) == 2)


## 최대공약수
def get_GCD(a, b):
    c = get_divisors(a) & get_divisors(b)
    return max(c)


## 최소공배수
def get_LCM(a, b):
    g = get_GCD(a, b)
    return (a*b)//g


## 소인수분해 
# -> 소수가 아닌 수가 들어갈 수 있다고 생각했는데,
# -> 이미 앞에서 다 나누어 떨어져서 그럴수가 없음
# => 이해 안가면 외우자.
def get_primes(n):
    primes = []
    for i in range(2, n+1):
        while n % i == 0:
            primes.append(i)
            n //= i
    return primes


## 에라토스테네스의 체 알고리즘
N = 120
is_prime = [True] * (N+1)   # 일단 모두 소수라고 간주하고 True를 가진 120번까지의 배열을 만듦
is_prime[1] = False     # 1은 소수가 아니니까 False

for i in range(2, int(sqrt(N))+1):
    if not is_prime[i]: continue    # 이미 소수가 아니라면 살펴볼 필요가 없음
    for j in range(2*i, N+1, i):    # 소수라면 배수들을 False로 만들어줌
        is_prime[j] = False


## 유클리드 알고리즘
# -> 외우는게 편할지도?
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
