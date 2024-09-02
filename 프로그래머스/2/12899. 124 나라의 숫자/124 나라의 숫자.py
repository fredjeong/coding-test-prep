def solution(n):
    answer = ""
    counter = 1
    while True:
        if n <= 3**counter:
            # 변환 시작
            n -= 1
            for i in reversed(range(counter)):
                if n // 3**i == 0: # 이 값은 0 또는 1또는 2이다 무조건
                    answer += "1"
                elif n // 3**i == 1:
                    answer += "2"
                elif n // 3**i == 2:
                    answer += "4"
                n %= 3**i
            break
        else:
            n -= 3**counter
            counter += 1
    return answer
