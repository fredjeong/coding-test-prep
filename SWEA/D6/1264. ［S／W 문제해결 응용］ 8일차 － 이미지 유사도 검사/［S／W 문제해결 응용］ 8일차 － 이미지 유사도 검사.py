T = int(input())

for test_case in range(1, T+1):
    n = int(input()) # 이미지 스캔 코드열의 크기
    x = "0" +input().strip()
    y = "0" + input().strip()

    """
    LCS (Longest Common Subsequence)
    """
    # (n+1)*(n+1) 행렬을 만든다
    # 이 때, 첫 번째 행과 열은 항상 0으로 맞추어준다.
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(n+1):
            if not i or not j:
                dp[i][j] = 0
            elif x[i] == y[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    cnt = dp[-1][-1]
    percentage = round(cnt/n * 100, 2)
    percentage = str(percentage)
    if percentage[-2] == ".":
        percentage += "0"

    print(f"#{test_case} {percentage}")