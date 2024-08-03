def solution(n):
    answer = 0
    d = 1
    while d <= n:
        if n % d == 0:
            answer += 1
            d += 1
        else:
            d += 1
    return answer