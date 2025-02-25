T = int(input())

for test_case in range(1, T+1):
    n = int(input()) # 배열의 크기 (1 <= n <= 100000)
    arr = list(map(int, input().split()))

    direction = None
    cnt = 1

    for i in range(1, n):
        # 다음 수 확인하고 현재 수와 비교
        # 아직 방향이 결정되지 않은 경우
        if not direction:
            # 값이 같은 경우 direction은 여전히 None으로 유지
            if arr[i] == arr[i-1]:
                pass
            elif arr[i] > arr[i-1]:
                direction = "ascending"
            elif arr[i] < arr[i-1]:
                direction = "descending"
        elif direction == "ascending":
            # 값이 같은 경우 direction 유지
            if arr[i] == arr[i-1]:
                pass
            # 오름차순 유지
            elif arr[i] > arr[i-1]:
                pass
            # 새 배열 생성
            elif arr[i] < arr[i-1]:
                cnt += 1
                direction = None
        elif direction == "descending":
            if arr[i] == arr[i-1]:
                pass
            elif arr[i] > arr[i-1]:
                cnt += 1
                direction = None
            elif arr[i] < arr[i-1]:
                pass

    print(f"#{test_case} {cnt}")