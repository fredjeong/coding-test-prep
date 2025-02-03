from collections import defaultdict
import heapq

T = int(input())

# 고객 만족도 설문지에 있는 접수 창구번호와 정비 창구번호를 이용하여 확인할 고객 정하기
for test_case in range(1, T+1):
    # n개의 접수 창구와 m개의 정비 창구가 있음
    n, m, num_customers, a_num, b_num = map(int, input().split())

    # 창구 번호가 0부터 시작하도록 수정
    a_num -= 1
    b_num -= 1

    reception_target = set() # a_num 접수창구를 이용한 고객들의 고객번호
    repair_target = set() # b_num 접수창구를 이용한 고객들의 고객번호

    # 접수 창구는 1부터 n까지, 정비 창구는 1부터 m까지 번호가 붙어 있음
    a = list(map(int, input().split())) # 접수 창구별 처리 시간
    b = list(map(int, input().split())) # 정비 창구별 처리 시간
    # 고객은 도착하는 대로 1번부터 고객번호를 부여받음
    k = list(map(int, input().split())) # 고객들의 도착 시간 목록

    # 도착 시간별 고객 번호 정리
    arrival_dic = defaultdict(list)
    for i in range(len(k)):
        arrival_dic[k[i]].append(i+1)

    # 접수창구 대기열 초기화
    new_customers = []
    heapq.heapify(new_customers)

    # 정비창구 대기열 초기화
    repair_customers = []

    reception = [0 for _ in range(n)] # 접수 창구별 받고 있는 고객 번호
    reception_waiting = [0 for _ in range(n)] # 접수 창구별 대기 시간
    repair = [0 for _ in range(m)] # 정비 창구별 받고 있는 고객 번호
    repair_waiting = [0 for _ in range(m)] # 정비 창구별 대기 시간

    # 매 시간 별 일어나는 일 확인
    timestep = 0

    count = 0
    while count < num_customers:
        # 해당 timestep에 도착한 고객이 있는지 확인
        if arrival_dic[timestep]:
            for customer in arrival_dic[timestep]:
                heapq.heappush(new_customers, customer)

        # 접수 창구, 정비 창구 대기시간 1씩 줄이기
        for i in range(n):
            if reception_waiting[i] > 0:
                reception_waiting[i] -= 1
                # 처리가 완료된 고객은 정비 창구 대기줄로 보내기
                if reception_waiting[i] == 0:
                    repair_customers.append((reception[i], i, timestep)) # 고객 번호, 접수 창구 번호, 온 시간

        for i in range(m):
            if repair_waiting[i] > 0:
                repair_waiting[i] -= 1
                # 처리과 완료된 고객은 카운트에 추가
                if repair_waiting[i] == 0:
                    count += 1

        # 고객이 도착했을 때 빈 접수 창구가 있는 경우 빈 접수 창구에서 고장 접수
        # 빈 접수 창구가 없는 경우 기다림
        # 접수 창구의 우선순위:
        #   1) 여러 고객이 기다리는 경우 고객번호가 낮은 순서대로
        #   2) 빈 창구가 여러 곳인 경우 창구번호가 작은 순서대로
        while 0 in reception_waiting and new_customers:
            reception_available = reception_waiting.index(0)
            reception[reception_available] = heapq.heappop(new_customers)
            reception_waiting[reception_available] += a[reception_available]

            # 타겟 창구에 고객이 온 경우 타겟 집합에 추가
            if reception_available == a_num:
                reception_target.add(reception[reception_available])

        # 정비 창구의 우선순위
        #   1) 먼저 기다리는 고객 우선
        #   2) 두 명 이상의 고객이 동시에 접수를 완료하고 정비 창구로 이동한 경우, 이용했던 접수 창구번호가 작은 고객 우선
        #   3) 빈 창구가 여러 곳인 경우 정비 창구번호가 작은 순서대로
        while 0 in repair_waiting and repair_customers:
            repair_available = repair_waiting.index(0)
            repair_customers = sorted(repair_customers, key=lambda x: [-x[2], -x[1]])
            repair[repair_available] = repair_customers.pop()[0]
            repair_waiting[repair_available] += b[repair_available]

            # 타겟 창구에 고객이 온 경우 타겟 집합에 추가
            if repair_available == b_num:
                repair_target.add(repair[repair_available])
        timestep += 1

    # 지갑을 분실한 고객과 같은 접수 창구와 같은 정비 창구를 이용한 고객의 고객번호들을 찾아 합 출력
    target = reception_target & repair_target
    if target:
        answer = sum(list(target))
    else:
        answer = -1
        
    print(f"#{test_case} {answer}")