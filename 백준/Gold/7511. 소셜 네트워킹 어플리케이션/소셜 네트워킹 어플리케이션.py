import sys
input = sys.stdin.readline


def find(node):
    # 루트노드 찾기
    if node != parent[node]:
        return find(parent[node])
    return node

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

T = int(input())

for test_case in range(1, T+1):
    print(f"Scenario {test_case}:")

    n = int(input()) # 노드의 수, 최대 10**6
    k = int(input()) # 간선의 수, 최대 10**5

    # 부모 노드
    parent = [i for i in range(n)]

    for _ in range(k):
        # 간선의 정보: a와 b는 연결되어 있다
        a, b = map(int, input().split())
        union(a, b)


    m = int(input()) # 구할 쌍의 수
    for _ in range(m):
        u, v = map(int, input().split())

        if find(u) == find(v):
            print(1)
        else:
            print(0)

    print()