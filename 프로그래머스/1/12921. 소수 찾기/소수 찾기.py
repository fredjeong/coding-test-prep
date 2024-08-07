def solution(n):
    # n 이하의 소수를 반환하는 에라토스테네스의 체 만들기
    arr = [True for _ in range(n+1)] # 0부터 n까지 저장
    for i in range(2, int(n ** 0.5)+1):
        if arr[i] == True:
            m = 2
            while i*m <= n:
                arr[i*m] = False
                m += 1    
    # n 이하의 수 중 소수의 개수 세기
    answer = 0
    for i in range(2, n+1):
        if arr[i] == True:
            answer +=1
    return answer