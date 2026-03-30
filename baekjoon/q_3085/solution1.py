def max_candy():
    global N, board
    max_cnt = 1

    # 행 선택
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j-1] == board[i][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt : max_cnt = cnt
    
    # 열 선택
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i-1][j] == board[i][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt : max_cnt = cnt
    
    return max_cnt

N = int(input())
board = [list(input()) for _ in range(N)]
ans = 0

# 가로 선택
for x in range(N):    
    for y in range(N-1):
        board[x][y], board[x][y+1] = board[x][y+1], board[x][y] # 옆에 있는 것 교환
        ans = max(max_candy(), ans)
        board[x][y], board[x][y+1] = board[x][y+1], board[x][y] # board 원래대로 돌리기

# 세로 선택
for y in range(N):    
    for x in range(N-1):
        board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
        ans = max(max_candy(), ans)
        board[x][y], board[x+1][y] = board[x+1][y], board[x][y]

print(ans)