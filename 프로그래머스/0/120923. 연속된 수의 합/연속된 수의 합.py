def solution(num, total):
    answer = []
    # 연속된 수 num개를 더하면 total이 된다.
    if num % 2 == 0: # 짝수
        mid = total // num
        for i in range(1, num//2 + 1):
            answer.append(mid - num//2 + i)
        for j in range(1, num//2+1):
            answer.append(mid + j)
        
    else: # 홀수
        mid = total // num
        for i in range(1, (num-1)//2 + 1):
            answer.append(mid - (num+1)//2 + i)
        answer.append(mid)
        for j in range(1, (num-1)//2 + 1):
            answer.append(mid + j)
    return answer