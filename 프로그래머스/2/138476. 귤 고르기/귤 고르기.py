def solution(k, tangerine):
    # 귤의 크기 별 개수를 정리
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    # 개수가 큰 순서대로 배열
    arr = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    
    answer = 0
    for i in range(len(arr)):
        k -= arr[i][1]
        answer += 1
        if k <= 0:
            break
    
    return answer
            
