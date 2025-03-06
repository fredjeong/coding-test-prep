import heapq
from collections import defaultdict

T = int(input())

for test_case in range(1, T+1):
    n, m, x = map(int, input().split())
    x -= 1

    parent_dic = defaultdict(set)
    dist_dic = defaultdict(int)

    dist_arr = [0 for _ in range(n)]

    for _ in range(m):
        start, end, dist = map(int, input().split())
        start -= 1
        end -= 1
        parent_dic[start].add(end)
        dist_dic[(start, end)] = dist

    """
    다익스트라 알고리즘을 이용해 x부터 모든 노드까지의 최단거리를 구한다
    """
    # 초기에는 모두 거리를 무한으로 설정한다
    come_dist = [1e9 for _ in range(n)]

    q = []
    # 시작 노드 초기화
    heapq.heappush(q, (0, x))
    come_dist[x] = 0

    while q:
        dist, cur_node = heapq.heappop(q)

        if dist > come_dist[cur_node]:
            continue

        for next_node in parent_dic[cur_node]:
            new_dist = dist_dic[(cur_node, next_node)] + come_dist[cur_node]
            if new_dist < come_dist[next_node]:
                come_dist[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

    for node in range(n):
        dist_arr[node] += come_dist[node]


    """
    다익스트라 알고리즘을 한 번 더 사용해 모든 노드부터 x까지의 최단거리를 구한다
    """
    for node in range(n):
        if node == x:
            continue

        # 초기에는 모두 거리를 무한으로 설정한다
        go_dist = [1e9 for _ in range(n)]

        q = []
        # 시작 노드 초기화
        heapq.heappush(q, (0, node))
        go_dist[node] = 0

        while q:
            dist, cur_node = heapq.heappop(q)

            if dist > go_dist[cur_node]:
                continue

            for next_node in parent_dic[cur_node]:
                new_dist = dist_dic[(cur_node, next_node)] + go_dist[cur_node]
                if new_dist < go_dist[next_node]:
                    go_dist[next_node] = new_dist
                    heapq.heappush(q, (new_dist, next_node))

        dist_arr[node] += go_dist[x]

    print(f"#{test_case} {max(dist_arr)}")
