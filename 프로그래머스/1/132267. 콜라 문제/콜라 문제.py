def solution(a, b, n):
    empty = n
    answer = 0
    while empty >= a:
        answer += (empty // a) * b
        empty = empty%a + (empty // a) * b
    return answer


