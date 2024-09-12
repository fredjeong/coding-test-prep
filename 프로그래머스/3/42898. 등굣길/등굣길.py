def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1
    dp[0][0] = 1
    for row in range(n):
        for col in range(m):
            if row == 0 and col == 0:
                continue
            if dp[row][col] == -1:
                continue
            if row == 0:
                if dp[row][col-1] == -1:
                    continue
                else:
                    dp[row][col] = dp[row][col-1]
            elif col == 0:
                if dp[row-1][col] == -1:
                    continue
                else:
                    dp[row][col] = dp[row-1][col]
            else:
                if dp[row-1][col] == -1 and dp[row][col-1] == -1:
                    continue
                
                if dp[row-1][col] == -1:
                    dp[row][col] = dp[row][col-1]
                elif dp[row][col-1] == -1:
                    dp[row][col] = dp[row-1][col]
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
            
                
    return dp[n-1][m-1]%1000000007