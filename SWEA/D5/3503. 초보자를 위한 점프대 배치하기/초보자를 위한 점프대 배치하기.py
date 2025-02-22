from collections import deque

T = int(input())

for test_case in range(1, T+1):
    n = int(input()) # 점프대의 수
    q = deque(sorted(map(int, input().split()), reverse=True)) # 점프대들의 높이
    max_val = q.popleft() # 최댓값

    max_diff = 0

    arr = deque([max_val])

    while q:
        num_1 = q.popleft()
        num_2 = None
        if q:
            num_2 = q.popleft()

        # 두 수가 존재한다면
        if num_2:
            # num_1와 양 끝, num_2와 양 끝을 비교한다
            num_1_left_dist = arr[0] - num_1
            num_1_right_dist = arr[-1] - num_1
            num_2_left_dist =  arr[0] - num_2
            num_2_right_dist = arr[-1] - num_2

            # 두 경우에 발생하는 최댓값이 적은 쪽으로 배치
            if max(num_1_left_dist, num_2_right_dist) < max(num_1_right_dist, num_2_left_dist):
                arr.appendleft(num_1)
                arr.append(num_2)
                max_diff = max([max_diff, num_1_left_dist, num_2_right_dist])
            else:
                arr.appendleft(num_2)
                arr.append(num_1)
                max_diff = max([max_diff, num_1_right_dist, num_2_left_dist])

        else:
            num_1_left_dist = arr[0] - num_1
            num_1_right_dist = arr[-1] - num_1
            arr.appendleft(num_1)
            max_diff = max([max_diff, num_1_left_dist, num_1_right_dist])

    print(f"#{test_case} {max_diff}")
