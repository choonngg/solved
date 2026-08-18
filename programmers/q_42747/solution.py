def solution(citations):
    citations = [-1] + sorted(citations)
    n = len(citations)

    start = [1e8 for _ in range(citations[-1] + 1)]
    for i in range(1, n):
        start[citations[i]] = min(i, start[citations[i]])
    for i in range(len(start)-2, -1, -1):
        start[i] = min(start[i], start[i+1])

    answer = -1
    for h in range(citations[-1] + 1):
        if n - start[h] >= h:
            answer = h
        else:
            break

    return answer

print(solution([100]))