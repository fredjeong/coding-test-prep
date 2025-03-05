import heapq

T = int(input())

for test_case in range(1, T+1):
    k = int(input())
    string = input().strip()

    # 부분 문자열을 모두 쪼개자
    q = set()

    n = len(string) # 부분 문자열의 길이
    for length in range(1, n+1):
        for i in range(n + 1 - length):
            q.add(string[i:i+length])
    q = list(q)
    heapq.heapify(q)

    if k > len(q):
        answer = "none"
    else:
        answer = heapq.nsmallest(k, q)[-1]

    print(f"#{test_case} {answer}")
