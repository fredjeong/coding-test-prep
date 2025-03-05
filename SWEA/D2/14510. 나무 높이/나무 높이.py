T = int(input())

for test_case in range(1, T+1):
    n = int(input()) # 나무의 개수 (최대 100)
    trees = list(map(int, input().split())) # 나무들의 높이

    max_height = max(trees) # 모든 나무가 max_height와 같아지도록 만들어야 함

    """
    arr[i]가 홀수인 i는 홀수 일이 홀수 번 껴있어야 함
    arr[i]가 짝수인 i는 홀수 일이 짝수 번 껴있어야 함
    """
    # 모든 나무들이 max_height가 되기 위해서 필요한 수
    for i in range(n):
        trees[i] = max_height - trees[i]

    min_odd_days = 0
    for num in trees:
        if num % 2:
            min_odd_days += 1

    # 홀수 일과 짝수 일 초기화
    odd_days = 0
    even_days = 0

    # 모두 홀수
    for num in trees:
        # 1일부터 묶는다
        quotient = num // 3

        # 홀짝이 공평하게 나뉘는 경우
        if num % 3 == 0:
            odd_days += quotient
            even_days += quotient
        elif num % 3 == 1:
            odd_days += quotient + 1
            even_days += quotient
        elif num % 3 == 2:
            odd_days += quotient
            even_days += quotient + 1


    if odd_days >= even_days + 2:
        while odd_days >= min_odd_days + 2 and odd_days >= even_days + 2:
            odd_days -= 2
            even_days += 1
    elif even_days >= odd_days + 2:
        while even_days >= odd_days + 2:
            even_days -= 1
            odd_days += 2

    # odd_days와 even_days가 같은 경우
    if odd_days == even_days:
        answer = odd_days + even_days


    elif even_days > odd_days:
        answer = even_days * 2
    else:
        answer = (odd_days - 1) * 2 + 1

    print(f"#{test_case} {answer}")
