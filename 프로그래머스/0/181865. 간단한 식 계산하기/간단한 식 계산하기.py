def solution(binomial):
    binomial = binomial.split(" ")
    
    a = int(binomial[0])
    op = binomial[1]
    b = int(binomial[2])
    
    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    else:
        answer = a * b
    
    return answer