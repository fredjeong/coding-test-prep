def solution(n):
    answer = 0
    m = str(bin(n))[2:].count("1")
    for num in range(n+1,1000000):
        if str(bin(num))[2:].count("1") == m:
            answer = num
            break

    return answer