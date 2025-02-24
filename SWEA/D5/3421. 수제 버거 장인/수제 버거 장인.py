T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    # 신메뉴를 개발하려 한다

    # i번 재료와 j번 재료가 동시에 포함된 버거는 만들 수 없다

    graph = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1

    # 만들 수 있는 버거의 종류가 몇 가지인지 구하여라
    total = 0
    
    def recursion(cur_node, comb):
        global total

        # 종료조건: cur_node가 n-1인 경우
        if cur_node == n-1:
            # history.add(comb)
            total += 1
            return

        # 넣거나 안넣거나
        can_add = True
        for node in comb:
            if graph[node][cur_node+1] or graph[cur_node+1][node]:
                can_add = False
                break
        if can_add:
            recursion(cur_node+1, comb + [cur_node+1])
        recursion(cur_node+1, comb)

    recursion(0, [])
    recursion(0, [0])

    print(f"#{test_case} {total}")
