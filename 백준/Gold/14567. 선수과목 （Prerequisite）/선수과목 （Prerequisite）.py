def solve_dp():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    dp = [1] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    for i in range(1, n + 1):
        for j in graph[i]:
            dp[j] = max(dp[j], dp[i] + 1)

    print(" ".join(map(str, dp[1:])))

solve_dp()