def solution(n, k):
    # 리스트 만들기
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
        # k가 (n-1)! * i 이하면 첫 번째 자리는 arr[i-1]이다
        # 따라서 
        
        # n=4인 경우
        # [1, 2, 3, 4]
        # [1, 2, 4, 3]
        # [1, 3, 2, 4]
        # [1, 3, 4, 2]
        # [1, 4, 2, 3]
        # [1, 4, 3, 2]
        # [2, 1, 3, 4]
        # k=7이라면?
        # 첫 번째 자리는 2인거 ㅇㅋ
        # 그 다음엔?
        # 남은 애들 중에서 k-(n-1)!*(i-1)번째를 뽑는다
    
def factorial(n):
    temp = 1
    for i in range(1, n+1):
        temp *= i
    return temp
    
#from itertools import permutations
#
#def solution(n, k):
#    temp = permutations(range(1, n+1)) 
#    answer = list(temp)[k-1]
#    
#    return answer