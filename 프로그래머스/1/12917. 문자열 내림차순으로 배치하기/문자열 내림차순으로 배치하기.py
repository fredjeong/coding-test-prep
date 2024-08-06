def solution(s):
    answer = ""
    capital = ""
    lower = ""
    for i in s:
        if i == i.lower():
            lower += i
        else:
            capital += i
    capital = sorted(capital, reverse = True)
    lower = sorted(lower, reverse = True)
    arr = lower + capital
    for i in arr:
        answer += i
    return answer