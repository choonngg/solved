def diff_count(start_n, start_m, start_8x8):
    global arr
    cnt = 0
    for i in range(8):
        for j in range(8):
            if arr[start_n+i][start_m+j] != start_8x8[i][j]:
                cnt += 1
    return cnt

N,M = map(int, input().split())
arr = [input() for _ in range(N)]
b_start_8x8 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
w_start_8x8 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]

min_cnt = 1e8
for start_n in range(N-8+1):
    for start_m in range(M-8+1):
        start_b_cnt = diff_count(start_n, start_m, b_start_8x8)
        start_w_cnt = diff_count(start_n, start_m, w_start_8x8)

        if start_b_cnt > start_w_cnt: cnt = start_w_cnt
        else: cnt = start_b_cnt

        if min_cnt > cnt:
            min_cnt = cnt

print(min_cnt)