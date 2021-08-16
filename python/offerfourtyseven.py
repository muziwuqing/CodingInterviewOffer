def maxValue(grid):
    if len(grid) == 0:
        return 0
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dp[0][0] = grid[0][0]
    for i in range(1, len(grid[0])):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for j in range(1, len(grid)):
        dp[j][0] = dp[j-1][0] + grid[j][0]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[len(grid)-1][len(grid[0])-1]


grid =[[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(maxValue(grid))
