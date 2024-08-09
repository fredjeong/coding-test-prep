def solution(num_list):
    prod = 1
    for i in num_list:
        prod *= i
    if prod < sum(num_list) ** 2:
        answer = 1
    else:
        answer = 0
    return answer