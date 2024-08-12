def solution(m, n, puddles):
    grid = [[1 for _ in range(m)] for _ in range(n)]
    # puddle 좌표
    for x, y in puddles:
        if x == 1:
            for i in range(y-1, n):
                grid[i][0] = 0
        elif y == 1:
            for i in range(x-1, m):
                grid[0][i] = 0
        else:
            grid[y-1][x-1] = 0
    # 경우의 수
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j]:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[-1][-1]%1000000007