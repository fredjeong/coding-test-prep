def solution(polynomial):
    polynomial = polynomial.split(" + ")
    x_term = []
    constant = []
    
    for i in polynomial:
        if 'x' in i:
            if i == 'x':
                x_term.append(1)
            else:
                x_term.append(int(i[:-1]))
        else:
            constant.append(int(i))

    x_final = sum(x_term)
    constant_final = sum(constant)
    
    if x_final == 0:
        answer = str(constant_final)
    elif x_final == 1:
        if constant_final == 0:
            answer = 'x'
        else:
            answer = 'x' + ' + ' + str(constant_final)
    else:
        if constant_final == 0:
            answer = str(x_final) + 'x'
        else:
            answer = str(x_final) + 'x' + ' + ' + str(constant_final)

    return answer