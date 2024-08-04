def solution(balls, share):
    n_factorial = 1
    k_factorial = 1
    n_k_factorial = 1
    for i in range(1,balls+1):
        n_factorial *= i
    for j in range(1, share+1):
        k_factorial *= j
    for k in range(1, balls-share+1):
        n_k_factorial *= k
    answer = n_factorial/(k_factorial * n_k_factorial)
    return answer