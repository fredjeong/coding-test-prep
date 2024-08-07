#def solution(number, limit, power):
#    answer = 0
#    
#    array = [True for i in range(number+1)]
#    prime = []
#
#    #에라토스테네스의 체 알고리즘
#    for i in range(2, int(number ** 0.5) + 1):
#        if array[i] == True:
#            j = 2
#            while i * j <= number:
#                array[i*j] = False
#                j += 1
#    for i in range(2, number+1):
#        if array[i]:
#            prime.append(i)
#                
#    for i in range(1, number+1):
#        if i == 1:
#            answer += 1
#            print(f"{i}: 1")
#        elif i not in prime: # 소수와 1을 제외한 나머지 모든 수
#            divisor = 1 # 자기 자신은 약수로 포함한다
#            for j in range(1, i//2 + 1): # 자기 자신을 제외한 가장 큰 약수는 i//2를 넘을 수 없다
#                if i % j == 0:
#                    divisor += 1
#                if divisor > limit:
#                    break
#            if divisor > limit: 
#                answer += power
#                #print(f"{i}: 소수 아니고 1 아님 - 약수 개수: {divisor}")
#            else:
#                answer += divisor
#                #print(f"{i}: 소수 아니고 1 아님 - 약수 개수: {divisor}")
#        else: 
#            answer += 2
#            #print(f"{i}: 소수")
#    return answer

def solution(number, limit, power):
    answer = 0
    # 시간복잡도
    # 검토해야 하는 모든 수: range(1, len(number) + 1)
    for i in range(1, number+1):
        # 1의 약수는 1 하나 밖에 없다 -> answer += divisor
        if i == 1:
            answer += 1
        # 소수인 경우
        else:
            divisor = 0
            for j in range(1, int(i**0.5)+1):
                if i%j == 0:
                    if i//j > j: # j보다 큰 수를 곱해야 하면 -> 페어가 만들어지면
                        divisor += 2
                    elif i//j == j:
                        divisor += 1
                
                if divisor > limit:
                    break
            if divisor > limit:
                answer += power
            else:
                answer += divisor
                    
                

        # case에서 자기 자신을 제외한 약수는 case//2 이하이다 
    # 소수는 무조건 약수가 2개이다 -> answer += divisor
    # 1의 약수는 1 하나 밖에 없다 -> answer += divisor
    return answer
