from collections import defaultdict, deque

T = int(input())

for test_case in range(1, T+1):
    v, e, node_1, node_2 = map(int, input().split())
    edges = list(map(int, input().split()))

    parent_dic = defaultdict(set)
    child_dic = defaultdict(int)

    for i in range(e):
        # 시작점 2*i, 도착점 2*i+1
        parent_dic[edges[2*i]].add(edges[2*i+1])
        child_dic[edges[2*i+1]] = edges[2*i]

    # node_1 조상들 정리
    ancestors_1 = set()
    q_1 = deque()
    q_1.append(node_1)

    while q_1:
        node = q_1.popleft()

        # 이미 검토했다면 스킵
        if node in ancestors_1:
            continue
        ancestors_1.add(node)

        # 부모 노드 찾기
        q_1.append(child_dic[node])

    # node_2 조상들 정리
    ancestors_2 = set()
    q_2 = deque()
    q_2.append(node_2)
    while q_2:
        node = q_2.popleft()

        # 만약 노드가 ancestors_1에 있다면 공통 조상이라는 뜻
        if node in ancestors_1:
            common_ancestor = node
            break

        # 이미 검토했다면 스킵
        if node in ancestors_2:
            continue
        ancestors_2.add(node)

        # 부모 노드 찾기
        q_2.append(child_dic[node])

    # 공통 조상으로부터 parent_dic 통해서 집합 구성
    descendants = set()

    q = deque()
    q.append(common_ancestor)

    while q:
        node = q.popleft()

        descendants.add(node)

        # 자식 노드 모두 추가
        for child in parent_dic[node]:
            if child in descendants:
                continue
            q.append(child)

    print(f"#{test_case} {common_ancestor} {len(descendants)}")
