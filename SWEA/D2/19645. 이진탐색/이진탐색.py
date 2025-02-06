def find_page(obj, left, right, count):
    # 중간 페이지 계산
    centre = int((left + right)/2)

    # 찾는 쪽 번호가 centre와 같아지면 탐색 종료
    if centre == obj:
        return count
    elif centre < obj:
        return find_page(obj, centre, right, count+1)
    else:
        return find_page(obj, left, centre, count+1)

T = int(input())

for test_case in range(1, T+1):
    p, a, b = map(int, input().split())

    count_a = find_page(a, 1, p, 0)
    count_b = find_page(b, 1, p, 0)

    if count_a < count_b:
        answer = "A"
    elif count_a > count_b:
        answer = "B"
    else:
        answer = "0"

    print(f"#{test_case} {answer}")