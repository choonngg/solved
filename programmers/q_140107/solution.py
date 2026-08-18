from math import sqrt

def solution(k, d):
    answer = 0
    
    for y in range(d+1):
        y = y * k
        if y > d: break

        max_x = int(sqrt(d**2 - y**2))
        x = max_x // k
        print(x, y)
        answer = answer + x + 1

    return answer

print(solution(2,4))