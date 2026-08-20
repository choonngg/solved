def solution(dirs):
    check = [[[0,0,0,0] for _ in range(11)] for _ in range(11)]    # ([5][5]가 원점) / [y][x][U,D,L,R]
    x = 5; y = 5

    answer = 0
    for c in dirs:
        if c == 'U':
            if y - 1 < 0:
                continue
            else:
                y -= 1
                if check[y][x][0] == 1 and check[y + 1][x][1] == 1:
                    continue
                else:
                    check[y][x][0] = 1; check[y + 1][x][1] = 1
                    answer += 1
        elif c == 'D':
            if y + 1 > 10:
                continue
            else:
                y += 1
                if check[y][x][1] == 1 and check[y - 1][x][0] == 1:
                    continue
                else:
                    check[y][x][1] = 1; check[y - 1][x][0] = 1
                    answer += 1
        elif c == 'L':
            if x - 1 < 0:
                continue
            else:
                x -= 1
                if check[y][x][2] == 1 and check[y][x + 1][3] == 1:
                    continue
                else:
                    check[y][x][2] = 1; check[y][x + 1][3] = 1
                    answer += 1
        elif c == 'R':
            if x + 1 > 10:
                continue
            else:
                x += 1
                if check[y][x][3] == 1 and check[y][x - 1][2] == 1:
                    continue
                else:
                    check[y][x][3] = 1; check[y][x - 1][2] = 1
                    answer += 1

    return answer

print(solution("LULLLLLLU"))