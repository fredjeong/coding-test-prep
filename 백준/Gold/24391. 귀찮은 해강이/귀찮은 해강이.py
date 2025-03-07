import sys
input = sys.stdin.readline

from collections import defaultdict

def union(a, b):
    # a번 노드와 b번 노드 합치기
    root_a = root_dic[a]
    root_b = root_dic[b]

    if root_a < root_b:
        # root_dic[b] = root_a
        for elem in children_dic[root_b]:
            root_dic[elem] = root_a
        children_dic[root_a] |= children_dic[root_b]
        children_dic.pop(root_b)
    elif root_a > root_b:
        # root_dic[a] = root_b
        for elem in children_dic[root_a]:
            root_dic[elem] = root_b
        children_dic[root_b] |= children_dic[root_a]
        children_dic.pop(root_a)
    else:
        pass

# 루트 노드에 연결된 노드들
children_dic = defaultdict(set)

# 자식을 키로, 루트 노드를 밸류로 하는 딕셔너리
root_dic = defaultdict(int)

n, m = map(int, input().split())

for node in range(1, n+1):
    # 루트 노드에 연결된 노드들
    children_dic[node].add(node)

    # 루트 노드 자기 자신으로 초기화
    root_dic[node] = node

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

# print(children_dic)
# print(root_dic)

cnt = 0
schedule = list(map(int, input().split()))
for idx in range(n-1):
    # i번 건물에서 i+1번 건물로 이동
    if root_dic[schedule[idx]] != root_dic[schedule[idx+1]]:
        cnt += 1

print(cnt)