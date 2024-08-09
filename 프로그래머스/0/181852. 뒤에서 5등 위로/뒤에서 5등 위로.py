def solution(num_list):
    num_list.sort()
    answer = sorted(num_list)[5:]
    return answer