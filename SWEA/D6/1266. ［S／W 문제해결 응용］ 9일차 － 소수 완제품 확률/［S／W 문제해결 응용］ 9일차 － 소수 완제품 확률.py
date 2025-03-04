from collections import defaultdict

T = int(input()) # 테스트 케이스의 개수

for test_case in range(1, T+1):
    a, b = map(int, input().split()) # 퍼센트로 주어진 확률

    # 0과 1 사이의 확률로 변환
    a /= 100
    b /= 100

    # 17 이하의 소수
    primes = {2, 3, 5, 7, 11, 13, 17}
    dic_a = defaultdict(float)
    dic_b = defaultdict(float)

    # 재귀를 이용하여 A 장인과 B 장인이 만드는 모든 경우들을 구하고, 이들 중 소수가 아닌 경우들은 따로 정리해둔다
    def recursion(person, idx, cnt, cum_prob):
        global probs_a, probs_b
        # A 장인이 만드는 모든 경우
        if person == "a":
            if idx == 18:
                # 마지막 사람까지 왔다면 저장하고 넘어간다
                if cnt not in primes:
                    dic_a[cnt] += cum_prob
                return
            recursion(person, idx+1, cnt+1, cum_prob * a)
            recursion(person, idx+1, cnt, cum_prob * (1- a))
        elif person == "b":
            if idx == 18:
                # 마지막 사람까지 왔다면 저장하고 넘어간다
                if cnt not in primes:
                    dic_b[cnt] += cum_prob
                return
            recursion(person, idx+1, cnt+1, cum_prob * b)
            recursion(person, idx+1, cnt, cum_prob * (1- b))

    recursion("a", 0, 0, 1)
    recursion("b", 0, 0, 1)

    # 누적합 구하기
    total_prob = 1

    for prob_a in dic_a.values():
        for prob_b in dic_b.values():
            total_prob -= prob_a*prob_b
    total_prob = round(total_prob, 6)
    if len(str(total_prob)) != 8:
        total_prob = str(total_prob) + "0"*(8-len(str(total_prob)))
    print(f"#{test_case} {total_prob}")