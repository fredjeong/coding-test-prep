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

n = int(input())

for node in range(1, n+1):
    # 루트 노드에 연결된 노드들
    children_dic[node].add(node)

    # 루트 노드 자기 자신으로 초기화
    root_dic[node] = node

for _ in range(n-2):
    a, b = map(int, input().split())
    union(a, b)

# print(children_dic)
# print(root_dic)
answer = " ".join(map(str, list(children_dic.keys())))
print(answer)