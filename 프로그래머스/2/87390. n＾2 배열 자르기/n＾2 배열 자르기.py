def solution(n, left, right):  
    answer = []
    for i in range(left, right+1):
        row = i // n + 1
        column = i % n + 1
        answer.append(max(row, column))
    return answer

# 시간 초과
#def solution(n, left, right):
#    answer = []
#    arr = [[0 for _ in range(n)] for _ in range(n)]
#    for i in range(n+1):
#        for j in range(i):
#            for k in range(i):
#                if arr[j][k] == 0:
#                    arr[j][k] = i
#        new_arr = []
#        for row in range(n):
#            new_arr += arr[row]
#        new_arr = new_arr[left:right+1]
#    return new_arr