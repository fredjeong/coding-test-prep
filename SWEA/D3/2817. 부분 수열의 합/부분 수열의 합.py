T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0

    def dfs(cur_node, total):
        global count

        # 합이 k와 같다면 경우의 수를 추가하고 종료
        if total == k:
            count += 1
            return

        # 합이 k를 초과했다면 종료
        if total > k:
            return

        for new_node in range(cur_node+1, n):
            dfs(new_node, total+arr[new_node])

    for cur_node in range(n):
        dfs(cur_node, arr[cur_node])

    print(f"#{test_case} {count}")
