def solution(n):
    tri = '+'
    # 제한사항: 1 <= n <= 100000000은 3**16과 3**17 사이이므로 3**17보다 큰 값은 존재하지 않음
    # 삼진법 반전
    for i in range(1, 18):
        if n % (3**i) != 0:
            temp = n % (3**i)
            tri += str(temp // (3**(i-1)))
            n -= temp
            if n == 0:
                break
        else:
            tri += '0'
            
    # 10진법 변환
    tri = str(int(tri))
    answer = 0
    for i in range(1,len(tri)+1):
        answer += int(tri[-i])*(3**(i-1))
    return answer