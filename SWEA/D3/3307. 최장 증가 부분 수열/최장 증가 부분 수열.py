T = int(input())

for test_case in range(1, T+1):
    n = int(input()) # 수열의 길이
    arr = list(map(int, input().split()))

    dp = [1 for _ in range(n)]

    for cur_node in range(n):
        for next_node in range(cur_node+1, n):
            if arr[next_node] >= arr[cur_node]:
                dp[next_node] = max(dp[cur_node]+1, dp[next_node])

    print(f"#{test_case} {max(dp)}")