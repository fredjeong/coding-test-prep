T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            x_i, y_i = xs[i], ys[i]
            x_j, y_j = xs[j], ys[j]
            dist = (x_i - x_j) ** 2 + (y_i - y_j) ** 2
            graph[i][j] = dist
            graph[j][i] = dist

    e = float(input())

    # 0번 노드부터 시작
    s_1 = {0}
    s_2 = {i for i in range(1, n)}
    cum_dist = 0
    while s_2:
        min_dist = float("inf")
        min_node = None
        for i in s_1:
            for j in s_2:
                dist = graph[i][j]

                if dist < min_dist:
                    min_dist = dist
                    min_node = j
        if min_node:
            s_2.discard(min_node)
            s_1.add(min_node)
            cum_dist += min_dist

    print(f"#{test_case} {round(cum_dist * e)}")