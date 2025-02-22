def recursion(idx, dist, visited):
    global min_dist
    # 종료조건
    if dist >= min_dist:
        return

    if len(visited) == n:
        # 마지막 고객에서 집으로 가는 길
        home_dist = abs(customers[idx][0] - home_x) + abs(customers[idx][1] - home_y)
        dist += home_dist
        min_dist = min(min_dist, dist)
        return

    # 아직 방문하지 않은 모든 고객에 대하여 조사
    for next_idx in range(n):
        if next_idx in visited:
            continue
        # 현재 고객에서 다음 고객까지의 거리
        temp_dist = abs(customers[idx][0] - customers[next_idx][0]) + abs(customers[idx][1] - customers[next_idx][1])
        recursion(next_idx, dist + temp_dist, visited | {next_idx})

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    company_x, company_y = arr[0], arr[1]
    home_x, home_y = arr[2], arr[3]
    customers = []
    for i in range(n):
        customers.append([arr[4+2*i], arr[5+2*i]])

    # 회사에서 출발하여 N명의 고객을 모두 방문하고 집으로 돌아오는 경로 중 가장 짧은 것
    # 고객은 최대 10명

    min_dist = 1e9

    # 모든 고객에 대해 조사
    for init_idx in range(n):
        work_dist = abs(company_x - customers[init_idx][0]) + abs(company_y - customers[init_idx][1])
        recursion(init_idx, work_dist, {init_idx})

    print(f"#{test_case} {min_dist}")