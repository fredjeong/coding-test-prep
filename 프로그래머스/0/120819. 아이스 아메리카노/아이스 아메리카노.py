def solution(money):
    n = money // 5500
    change = money - n * 5500
    answer = [n, change]
    return answer