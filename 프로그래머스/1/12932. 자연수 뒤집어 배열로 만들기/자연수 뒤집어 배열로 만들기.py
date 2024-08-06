def solution(n):
    n = str(n)
    n_reversed = n[::-1]
    answer = []
    for i in n_reversed:
        answer.append(int(i))
    return answer