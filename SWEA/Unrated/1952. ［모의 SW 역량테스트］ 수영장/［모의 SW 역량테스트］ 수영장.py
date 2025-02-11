T = int(input())

for test_case in range(1,T+1):
    # 1일, 1달, 3달, 1년 이용권 요금
    fares = list(map(int, input().split()))

    # 1월부터 12월까지의 이용 계획
    plan = list(map(int, input().split()))

    # 여러 옵션의 비용을 리스트로 관리
    min_cost = 1e9

    """
    일 년 이용권만 구매하는 경우
    """
    min_cost = min(min_cost, fares[-1])

    """
    3개월 이용권을 구매하지 않는 경우
    """
    temp_cost = 0
    for month in range(12):
        temp_cost += min(plan[month] * fares[0], fares[1])
    min_cost = min(min_cost, temp_cost)

    """
    3개월 이용권, 1개월 이용권, 1일 이용권을 섞어서 사용하는 경우
    """
    # 3개월 이용권을 하나만 사용하는 경우
    for i in range(10):
        temp_cost = fares[2]
        coverage = {i, i+1, i+2}
        for month in range(12):
            if month in coverage:
                continue
            temp_cost += min(plan[month] * fares[0], fares[1])
        min_cost = min(min_cost, temp_cost)

    # 3개월 이용권을 두 개 사용하는 경우
    for i in range(9):
        for j in range(i+1, 10):
            temp_cost = fares[2]*2
            coverage = {i, i+1, i+2, j, j+1, j+2}
            for month in range(12):
                if month in coverage:
                    continue
                temp_cost += min(plan[month] * fares[0], fares[1])
            min_cost = min(min_cost, temp_cost)

    # 3개월 이용권을 세 개 사용하는 경우
    for i in range(8):
        for j in range(i+1, 9):
            for k in range(j+1, 10):
                temp_cost = fares[2]*3
                coverage = {i, i+1, i+2, j, j+1, j+2, k, k+1, k+2}
                for month in range(12):
                    if month in coverage:
                        continue
                    temp_cost += min(plan[month] * fares[0], fares[1])
                min_cost = min(min_cost, temp_cost)

    # 3개월 이용권을 네 개 사용하는 경우
    min_cost = min(min_cost, fares[2]*4)

    print(f"#{test_case} {min_cost}")