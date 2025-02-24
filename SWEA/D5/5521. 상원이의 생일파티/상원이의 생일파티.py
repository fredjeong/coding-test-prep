from collections import defaultdict

T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    dic = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)


    visited = set()

    for friend_1 in dic[1]:
        visited.add(friend_1)
        visited |= set(dic[friend_1])

    visited.discard(1)
    print(f"#{test_case} {len(visited)}")