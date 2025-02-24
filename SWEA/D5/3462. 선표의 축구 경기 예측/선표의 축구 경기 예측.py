def comb_count(n):
    numerator = 1
    denominator = 1
    for i in range(n):
        numerator *= 30 - i
        denominator *= (i+1)
    return numerator // denominator

# 30개 중에 n개 선택하는 경우의 수
dic = {}
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
for num in primes:
    dic[num] = comb_count(num)

def bernoulli(n, prob):
    # 30Cn * (prob ** n) * (1-prob)**(30-n)
    return dic[n] * (prob ** n) * ((1-prob)**(30-n))

T = int(input())

for test_case in range(1, T+1):
    prob_a, prob_b = map(int, input().split())
    prob_a *= 0.01
    prob_b *= 0.01

    # 한 경기는 30개의 간격으로 나누어진다
    # 1 - 두 팀이 모두 소수 득점을 못할 확률
    # 30 이하의 소수

    # 경우의 수가 2**30이므로 재귀 방식으로 완전탐색은 불가
    # 각 팀이 넣을 수 있는 골은 최대 30골이다
    # 결국 조합 경우의 수를 뽑는 것
    # 베르누이 이용
    total_prob_a = 0
    total_prob_b = 0
    for n in primes:
        total_prob_a += bernoulli(n, prob_a)
        total_prob_b += bernoulli(n, prob_b)

    answer = round(1 - (1 - total_prob_a)*(1 - total_prob_b), 5)
    if len(str(answer)) != 7:
        answer = str(answer) + "0"*(7-len(str(answer)))
    print(f"#{test_case} {answer}")