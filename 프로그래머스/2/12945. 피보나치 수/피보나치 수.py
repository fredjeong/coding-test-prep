def solution(n):    
    arr = [0, 1]
    for i in range(n):
        f = arr[-1] + arr[-2] # i + 2번째 피보나치 수
        arr.append(f)
    
    answer = arr[n] % 1234567
    
    return answer