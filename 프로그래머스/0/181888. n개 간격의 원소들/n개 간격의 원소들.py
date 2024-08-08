def solution(num_list, n):
    answer = []
    for i in range(len(num_list)):
        if n*i < len(num_list):
            answer.append(num_list[n*i])
    return answer