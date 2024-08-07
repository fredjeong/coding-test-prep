def solution(n, m, section):
    count = 1
    start = section[0]
    for i in section:
        if start + (m - 1) < i:
            start = i
            count += 1 
    return count