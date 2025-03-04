import heapq

def GCD(p, q):
    if p < q:
        return GCD(q, p)
    elif q == 0:
        return p
    else:
        return GCD(q, p % q)

def get_slope(a, b):
    # a와 b는 튜플로 주어진다
    if b[0] == a[0]:
        if b[1] > a[1]:
            return "+inf"
        else:
            return "-inf"
    elif b[1] == a[1]:
        if b[0] > a[0]:
            return "+0"
        else:
            return "-0"
    else:
        if b[1]-a[1] > 0 and b[0]-a[0] > 0:
            sign = "up-right"
        elif b[1]-a[1] > 0 and b[0]-a[0] < 0:
            sign = "up-left"
        elif b[1]-a[1] < 0 and b[0]-a[0] > 0:
            sign="down-right"
        else:
            sign = "down-left"
        gcd = GCD(abs(b[1]-a[1]), abs(b[0]-a[0]))
        # 여기서 최대공약수 함수를 사용하는 것
        return sign + str(abs(b[1]-a[1])//gcd) + "/" + str(abs(b[0]-a[0])//gcd)

T = int(input())

for test_case in range(1, T+1):
    r, n, k = map(int, input().split()) # 격자판의 크기, 로봇의 수, 상수
    robots_arr = []
    for _ in range(n):
        # 각 로봇의 좌표
        row, col = map(int, input().split())
        row -= 1
        col -= 1
        robots_arr.append((row, col))

    """
    첫 번째 문제
    한 점에서 다른 모든 점 사이의 기울기를 구하고,
    이들을 집합에 넣는다
    마지막으로 집합의 길이를 배열 A에 넣는다
    """
    A = []

    for robot in range(n):
        s = set()
        for target in range(n):
            if robot == target:
                continue
            s.add(get_slope(robots_arr[robot], robots_arr[target]))
        A.append(len(s))

    answer_1 = sum(A)

    """
    두 번째 문제
    만들어진 A를 작은 순으로 계속 정렬해야 하므로,
    새로운 우선순위 큐 A_prime을 정의하고,
    한 사이클이 돌 때마다 A_prime의 가장 작은 값 n개를 빼서 A로 새로 정의한다.
    """

    C = 0
    for _ in range(n):
        A_prime = []
        heapq.heapify(A_prime)

        for j in range(1, n+1):
            temp = ((A[j-1] * k + j) % n) + 1
            heapq.heappush(A_prime, temp)
            heapq.heappush(A_prime, ((temp * j + k) % n) + 1)

        A = heapq.nsmallest(n, A_prime)

        B = 1
        for j in range(1, 2*n+1):
            A_pop = heapq.heappop(A_prime)
            B = ((B * A_pop) + j) % n + 1
        C += B

    answer_2 = C

    print(f"#{test_case} {answer_1} {answer_2}")