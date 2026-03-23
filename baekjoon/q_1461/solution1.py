## 1) 양수, 음수 개수 파악
## 2) 절대값 순으로 내림차순 정렬
## 3) 양수, 음수를 묶음으로 하고 (절대값의 최대)*2를 다 더해서 최대 걸음수를 구함
## 4) 최대 걸음수에서 가장 먼곳을 가는 경우를 빼서 최소값 구함

N, M = map(int, input().split())

books = list(map(int, input().split()))
books = sorted(books, key = lambda x: abs(x), reverse = True)
plus_books = []
minus_books = []
for b in books:
    if b > 0: 
        plus_books.append(b)
    else: 
        minus_books.append(b)

plus_books = sorted(plus_books, key = lambda x : abs(x), reverse = True)
minus_books = sorted(minus_books, key = lambda x : abs(x), reverse = True)

max_steps = 0
for i in range(0, len(plus_books), M):
    max_steps += 2 * abs(plus_books[i])
for i in range(0, len(minus_books), M):
    max_steps += 2 * abs(minus_books[i])

ans = max_steps - abs(books[0])
print(ans)
