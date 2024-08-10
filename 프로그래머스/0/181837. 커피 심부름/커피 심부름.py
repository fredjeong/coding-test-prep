def solution(order):
    answer = 0
    americano = 4500
    caffelatte = 5000
    for i in order:
        if "americano" in i:
            answer += 4500
        elif "latte" in i:
            answer += 5000
        else:
            answer += 4500
    return answer