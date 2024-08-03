def solution(num_list, n):
    answer = []
    key = len(num_list) // n
    for i in range(1,key+1):
        answer += [num_list[:n:]]
        num_list = num_list[-n*(key-i):]
    return answer