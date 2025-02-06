from collections import defaultdict

T = int(input())

for test_case in range(1, T+1):
    nums, n = input().split()
    n = int(n)
    nums = list(nums)

    visited = defaultdict(set)
    length = len(nums)
    max_val = 0

    def dfs(arr_, n_left):
        global max_val
        # 남은 교환 가능 횟수가 0이면 종료
        if not n_left:
            val = int("".join(arr_))
            max_val = max(max_val, val)
            return

        for idx_1 in range(length):
            for idx_2 in range(idx_1 + 1, length):
                # 배열 복사
                arr = arr_[:]

                # 값 교체
                arr[idx_1], arr[idx_2] = arr[idx_2], arr[idx_1]

                temp = "".join(arr)
                # visited에 있다면 스킵
                if temp in visited[n_left]:
                    continue
                # visited에 추가
                visited[n_left].add(temp)

                # 재귀함수 실행
                dfs(arr, n_left - 1)

    dfs(nums, n)
    print(f"#{test_case} {max_val}")