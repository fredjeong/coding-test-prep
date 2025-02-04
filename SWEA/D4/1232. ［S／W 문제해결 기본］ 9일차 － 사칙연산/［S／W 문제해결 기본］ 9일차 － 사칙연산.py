for test_case in range(1, 11):
    n = int(input()) # 정점의 개수

    tree_list = [None for _ in range(n+1)]
    children = {}

    # 중위 표기법으로 방문해야 함
    for _ in range(n):
        arr = list(input().split())

        # 정점이 연산자인 경우
        if len(arr) == 4:
            node_num = int(arr[0])
            operator = arr[1]
            tree_list[node_num] = operator
            left_child = int(arr[2])
            right_child = int(arr[3])
            children[node_num] = (left_child, right_child)

        # 정점이 정수인 경우
        else:
            node_num, val = map(int, arr)
            tree_list[node_num] = val

    # 뒤에서부터 보면서 연산자가 나오면 자식 노드 계산
    for i in range(n, 0, -1):
        # 자식 노드는 i*2, i*2+1
        if tree_list[i] == "+":
            tree_list[i] = tree_list[children[i][0]] + tree_list[children[i][1]]
        elif tree_list[i] == "-":
            tree_list[i] = tree_list[children[i][0]] - tree_list[children[i][1]]
        elif tree_list[i] == "*":
            tree_list[i] = tree_list[children[i][0]] * tree_list[children[i][1]]
        elif tree_list[i] == "/":
            tree_list[i] = tree_list[children[i][0]] // tree_list[children[i][1]]

    print(f"#{test_case} {tree_list[1]}")