from collections import defaultdict, deque

for test_case in range(1, 11):
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))

    order = [] # 작업 순서를 저장
    visited = set()

    """
    child_dic: 자식 노드를 키로 하는 딕셔너리
    parent_dic: 부모 노드를 키로 하는 딕셔너리
    """
    child_dic = defaultdict(set)
    parent_dic = defaultdict(set)

    for i in range(e):
        # 시작점: 2*i, 도착점: 2*i+1
        child_dic[edges[2*i+1]].add(edges[2*i])
        parent_dic[edges[2*i]].add(edges[2*i+1])


    # 일을 끝낼 수 있는 작업 순서 하나만 제시

    # 방향성이 있음 -> 딕셔너리 + dfs로 관리

    """
    자식 노드를 키로 하고, 부모 노드를 밸류로 한다면?
    for문을 이용해서 dic 안에 없는 노드라면 거기서 시작할 수 있음을 의미한다
    """

    q = deque()
    for node in range(1, v+1):
        # child_dic 안에 없는 노드라면 거기서 시작할 수 있음을 의미한다
        if node not in child_dic:
            q.append(node)

    while q:
        node = q.popleft()

        # 이미 방문한 노드라면 건너뛴다
        if node in visited:
            continue

        visited.add(node)
        order.append(node)


        # node 노드를 부모 노드로 하는 자식 child들에 대하여
        # 각 자식의 부모가 모두 visited에 있다면 조건 충족했으므로 큐에 추가
        for child in parent_dic[node]:
            if child in visited:
                continue
            if child_dic[child] & visited != child_dic[child]:
                continue
            q.append(child)

    print(f"#{test_case} {' '.join(map(str, order))}")

