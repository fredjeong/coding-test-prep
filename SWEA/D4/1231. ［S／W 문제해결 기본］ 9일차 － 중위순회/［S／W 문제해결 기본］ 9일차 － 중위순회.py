for test_case in range(1, 11):
    n = int(input())

    tree = [None for _ in range(n+1)]
    for _ in range(n):
        arr = list(input().split()) # 정점 정보
        node_num = int(arr[0])
        char = arr[1]
        tree[node_num] = char

    # in-order 방식으로 읽어야 함
    answer = ""
    def recursion(node_num):
        global answer

        if node_num*2 <= n:
            recursion(node_num*2)
        answer += tree[node_num]
        if node_num*2+1 <= n:
            recursion(node_num*2+1)

    recursion(1)

    print(f"#{test_case} {answer}")
