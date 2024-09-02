def solution(arrayA, arrayB):
    answer = [0, 0]

    # answer[0]에 추가하는 과정
    a = min(arrayA)
    divisors = findDivisors(a)
    for i in divisors:
        is_break = 0
        for j in arrayA:
            if j % i != 0:
                is_break = 1
                break
        if is_break == 1:
            continue
        
        for k in arrayB:
            if k % i == 0:
                is_break = 1
                break
        if is_break == 1:
            continue
        
        answer[0] = i
        break

    # answer[1]에 추가하는 과정
    a = min(arrayB)
    divisors = findDivisors(a)
    for i in divisors:
        is_break = 0
        
        for j in arrayB:
            if j % i == 0:
                pass
            else:
                is_break = 1
                break
        if is_break == 1:
            continue
        
        for k in arrayA:
            if k % i == 0:
                is_break = 1
                break
        if is_break == 1:
            continue
        
        answer[1] = i
        break
    
    answer = max(answer)
    return answer

def findDivisors(n):
    arr = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            arr.append(i) 
            if ((i**2) != n): 
                arr.append(n // i)
    arr.sort(reverse=True)
    return arr