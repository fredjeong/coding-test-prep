def solution(n, m):
    a = max(n, m)
    b = min(n, m)
    common_divisor = []
    lcm = 0
    
    # 최대공약수
    for i in range(1, b+1):
        if a%i == 0 and b%i == 0:
            common_divisor.append(i)
    gcd = max(common_divisor)
    
    # 최소공배수
    for i in range(a, a * b + 1):
        if i % a == 0 and i % b == 0:
            lcm = i
            break
    
    answer = [gcd, lcm]
    return answer