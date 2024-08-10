def solution(ineq, eq, n, m):
    tf = None
    if ineq == "<":
        if eq == "=":
            tf = n <= m
        else:
            tf = n < m
    else:
        if eq == "=":
            tf = n >= m
        else:
            tf = n > m
    if tf == True:
        answer = 1
    else:
        answer = 0
    return answer