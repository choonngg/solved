def valid_check(y, x, n):
    global board

    for i in range(9):
        if board[y][i] == n or board[i][x] == n:
            return False
    
    nx, ny = (x//3)*3, (y//3)*3
    for i in range(3):
        for j in range(3):
            if board[ny + i][nx + j] == n:
                return False
    
    return True

def search(lev):
    global board, zeros

    if lev == len(zeros):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end = " ")
            print()
        exit()

    y, x = zeros[lev]
    for n in range(1, 10):
        if valid_check(y, x, n):
            board[y][x] = n
            search(lev+1)
            board[y][x] = 0

board = []
board += [list(map(int, input().split())) for _ in range(9)]
zeros = [(y, x) for y in range(9) for x in range(9) if board[y][x] == 0]

search(0)