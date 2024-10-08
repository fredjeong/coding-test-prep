def solution(a, b):
    b = b / gcd(a,b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    
    if b == 1:
        answer = 1
    else:
        answer = 2
    return answer
        
def gcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b != 0:
        (a, b) = (b, a % b)
    return a