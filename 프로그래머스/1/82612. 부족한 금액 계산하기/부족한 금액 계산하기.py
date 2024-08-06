def solution(price, money, count):
    amount = 0
    for i in range(1, count+1):
        amount += price * i
    if money - amount >= 0:
        answer = 0
    else:
        answer = abs(money - amount)
    return answer