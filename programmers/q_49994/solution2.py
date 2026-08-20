def solution(dirs):
    x = 0; y = 0
    visited = set()

    direction = {
        'U' : (0, 1),
        'D' : (0, -1),
        'L' : (-1, 0),
        'R' : (1, 0)
    }

    for command in dirs:
        dx, dy = direction[command]
        nx, ny = x + dx, y + dy

        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        visited.add(tuple(sorted(((x, y), (nx, ny)))))

        x, y = nx, ny

    return len(visited)
