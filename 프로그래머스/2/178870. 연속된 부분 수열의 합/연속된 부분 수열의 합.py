from collections import deque

def solution(sequence, k):
    if k <= 1000:
        if k in sequence:
            idx = sequence.index(k)
            return [idx, idx]
    length = len(sequence)
    if length == 2:
        return [0,1]
    
    # 길이가 2인 부분수열부터 시작해보자
    start = 0   # 시작 인덱스
    end = 1     # 종료 인덱스
    
    temp = deque(sequence[start:end+1]) # sequence의 길이가 3 이상일 때이다
    total = sum(temp)
    temp_length = 2
    while total < k:
        if end+1 == length:
            break
        end += 1
        temp_length += 1
        temp.append(sequence[end])
        total += sequence[end]
    
    if total == k and (temp_length == 2 or temp_length == length):
        return [start, end]
    else:
        answer = [start, end]

#    if total > k:
#        while total > k:
#            total -= temp[0]
#            temp.popleft()
#            start += 1
#            temp_length -= 1
#        if total == k:
#            if total == k and (temp_length == 2 or temp_length == length):
#                return [start, end]
#            else:
#                answer = [start, end]
    
    # 일단 세이브하고 길이를 더 줄일 수 있는지 보자
    #answer = [start, end]
    #print(temp)
    # 합이 k인 애들만 남았음
    # 다음 과정을 반복한다
    is_break = 0
    while is_break == 0:      
        # 합이 k 미만이 되도록 맨 앞 원소를 자른다
        start += 1
        temp_length -= 1
        total -= temp[0]
        temp.popleft()

        # total >= k가 될 때까지 옆 칸으로 옮긴다
        # 단, 이 과정에서 끝에 도달하면 멈춘다
        while total < k:
            if end+1 == length:
                is_break = 1
                break
            start += 1
            end += 1
            total -= temp[0]
            total += sequence[end]
            temp.append(sequence[end])
            temp.popleft()

        # 깎는 과정이 있어야 함
        if temp_length == 2 and total == k:
            return [start, end]
        elif total == k and temp_length < answer[1]-answer[0]+1:
            answer = [start, end]
            #print(answer)
    return answer