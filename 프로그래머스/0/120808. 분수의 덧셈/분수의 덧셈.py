def solution(numer1, denom1, numer2, denom2):
    denominator = lcm(denom1, denom2)
    numerator_1 = numer1 * lcm(denom1, denom2)/denom1
    numerator_2 = numer2 * lcm(denom1, denom2)/denom2
    numer_sum = numerator_1 + numerator_2
    answer = [numer_sum / gcd(numer_sum, denominator), denominator / gcd(numer_sum, denominator)]
    return answer

def gcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b != 0:
        (a,b) = (b, a%b)
    return a

def lcm(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    return (a * b) / gcd(a, b)
