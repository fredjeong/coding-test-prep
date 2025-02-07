import heapq

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    q = []
    result = []

    for _ in range(n):
        arr = list(input().split())

        # 연산 1
        if arr[0] == "1":
            # arr[1]을 최대 힙에 추가한다
            heapq.heappush(q, -int(arr[1]))

        # 연산 2
        else:
            if q:
                # 현재 최대 힙의 루트 노드의 키값을 출력하고 해당 노드를 삭제한다
                result.append(str(-heapq.heappop(q)))
            else:
                # 힙에 원소가 없다면 -1 출력
                result.append("-1")

    answer = " ".join(result)
    print(f"#{test_case} {answer}")