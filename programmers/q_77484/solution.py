def solution(lottos, win_nums):
    count = 0; mn = 0; mx = 0
    max_rank = 0; min_rank = 0

    zero_count = 0
    for i in lottos:
        if i == 0: zero_count = zero_count + 1
    
    for i in lottos:
        for j in win_nums:
            if i == j: count = count + 1
    
    mn = count; mx = count + zero_count

    if mn == 6:
        min_rank = 1
    elif mn == 5:
        min_rank = 2
    elif mn == 4:
        min_rank = 3
    elif mn == 3:
        min_rank = 4
    elif mn == 2:
        min_rank = 5
    else:
        min_rank = 6

    if mx >= 6:
        max_rank = 1
    elif mx == 5:
        max_rank = 2
    elif mx == 4:
        max_rank = 3
    elif mx == 3:
        max_rank = 4
    elif mx == 2:
        max_rank = 5
    else:
        max_rank = 6

    answer = [max_rank, min_rank]
    return answer

print(solution([45, 4, 35, 20, 3, 9], 	[20, 9, 3, 45, 4, 35]))