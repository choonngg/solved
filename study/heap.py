from queue import PriorityQueue

# 최소힙이 default
pq = PriorityQueue()

# 삽입 -> 우선순위대로 정렬
pq.put(40); pq.put(30); pq.put(10); pq.put(20)

# 출력
print(pq.queue)

# 제거 -> 우선순위 높은것 먼저 제거
delete_element = pq.get()
print(delete_element)

# 제거하지않고 우선순위 높은거 확인
top_element = pq.queue[0]
print(top_element)

# 크기 확인
print(len(pq.queue))

# 비어있는지 확인
print(pq.empty())

print(pq.queue)

# 우선순위 큐 그냥 순회 -> 순서 보장 x
for u in pq.queue:
    print(u, end=" ")
print()

# 우선순위 큐 우선순위대로 순회
while pq.queue:
    print(pq.get(), end=" ")