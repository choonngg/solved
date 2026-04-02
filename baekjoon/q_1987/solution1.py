def search(y, x):
    global R, C, board, dx, dy, check, cur_len, ans

    if y<0 or x<0 or y>=R or x>=C :
        return
    if check[ord(board[y][x]) - ord('A')]:
        return
    
    cur_len += 1
    check[ord(board[y][x]) - ord('A')] = True
    ans = max(ans, cur_len)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        search(ny, nx)
    
    check[ord(board[y][x]) - ord('A')] = False
    cur_len -= 1
    

R, C = map(int, input().split())
board = [input() for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
check = [False] * 26
cur_len = 0
ans = 0

search(0,0)
print(ans)