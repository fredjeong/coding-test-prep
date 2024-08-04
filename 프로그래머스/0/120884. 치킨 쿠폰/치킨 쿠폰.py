def solution(chicken):
    coupons = chicken
    answer = 0
    
    while coupons >= 10:
        order = coupons // 10
        answer += order
        coupons = coupons % 10 + order
    return answer
