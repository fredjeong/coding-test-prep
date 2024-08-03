def solution(n):
    answer = 0
    factorial = 1
    for i in range(1, n+1):
        if factorial * i <= n:
            factorial *= i
            answer += 1
    return answer