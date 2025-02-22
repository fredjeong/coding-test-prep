from collections import defaultdict

def recursion(cur_idx, history, visited):
    global max_connections, max_history

    length = len(history)
    if length >= max_connections:
        max_connections = length
        max_history = history

    # 연결 조건: cur_idx의 암나사 굵기와 같은 굵기의 수나사를 가진 막대만 연결 가능
    required_thickness = total_dic[cur_idx][1]
    for next_idx in male_dic[required_thickness]:
        if next_idx in visited:
            continue
        recursion(next_idx, history + [next_idx], visited | {next_idx})

T = int(input())

for test_case in range(1, T+1):
    n = int(input()) # 원형 금속 막대의 개수
    arr = list(map(int, input().split())) # 2개씩 수나사 굵기와 암나사 굵기

    male_dic = defaultdict(list)
    female_dic = defaultdict(list)
    total_dic = defaultdict(tuple)

    for i in range(n):
        male = arr[2*i]
        female = arr[2*i+1]
        male_dic[male].append(i)
        female_dic[female].append(i)
        total_dic[i] = (male, female)

    max_connections = 0
    max_history = None

    for i in range(n):
        recursion(i, [i], {i})

    arr = []
    for i in max_history:
        arr += [total_dic[i][0], total_dic[i][1]]
    answer = " ".join(map(str, arr))
    print(f"#{test_case} {answer}")