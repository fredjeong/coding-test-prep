def solution(n, k):
    arr = [i for i in range(1, n+1)]
    answer = []
    
    while len(arr) > 0:
        for i in range(1, len(arr) + 1):
            fact = factorial(len(arr) - 1)
            if k <= fact * i:
                answer.append(arr[i-1])
                k -= fact * (i-1)
                del arr[i-1]
                break

    return answer
    
def factorial(n):
    temp = 1
    for i in range(1, n+1):
        temp *= i
    return temp

## 시간 초과
#from itertools import permutations
#
#def solution(n, k):
#    temp = permutations(range(1, n+1)) 
#    answer = list(temp)[k-1]
#    
#    return answer