def solution(n, t, m, p):
    if p == m:
        p = 0
    # 1, 2, 3, 4 등 차례대로 얘기하고 이를 n진법으로 바꾼다
    count = 0 # 십진법 숫자
    order = 1 # 차례
    result = ""
    
    if order % m == p:
        result += "0"
    
    while len(result) < t:
        count += 1
        # count를 n진법으로 표현
        output = convert(count, n)
        
        # 튜브의 순서를 계산
        for i in output:
            # 숫자 하나 말할 때마다 순서 추가
            order += 1 
            if order % m == p: # 튜브가 말할 차례
                result += i
                if len(result) == t:
                    break

    return result

def convert(number, n):
    # number: 십진법 숫자
    # n: 바꾸고 싶은 진법
    output = ""
    power = 0
    while number != 0:
        power += 1
        if number % (n ** power) // (n ** (power - 1)) == 10: 
            output += "A"
        elif number % (n ** power) // (n ** (power - 1)) == 11:
            output += "B"
        elif number % (n ** power) // (n ** (power - 1)) == 12:
            output += "C"
        elif number % (n ** power) // (n ** (power - 1)) == 13:
            output += "D"
        elif number % (n ** power) // (n ** (power - 1)) == 14:
            output += "E"
        elif number % (n ** power) // (n ** (power - 1)) == 15:
            output += "F"
        elif number % (n ** power) // (n ** (power - 1)) < 10:
            output += str(number % (n ** power) // (n ** (power - 1)))
        number -= number % (n ** power)
    
    return reversed(output)