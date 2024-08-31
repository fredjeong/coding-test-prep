def solution(numbers):
    answer = []
    for number in numbers:
        binary = "0" * (17 - len(bin(number)[2:])) + bin(number)[2:]
        while True:
            counter = 0
            number += 1
            new_binary = "0" * (17 - len(bin(number)[2:])) + bin(number)[2:]
            for i in reversed(range(len(binary))):
                if new_binary[i] != binary[i]:
                    counter += 1
            if counter > 2:
                continue
            answer.append(int('0b' + str(int(new_binary)), 2))
            break
    return answer
                
        
    
    
#    # numbers 안의 각 수에 대해서
#    for number in numbers:
#        # 1의 개수 세기
#        # 그보다 큰 수 중 비트가 다른 지점이 2개 이하인 수 추출
#        while True:
#            number +=1 
#            # 1의 개숙 
#            
#            
#            answer.append()
#    return answer

            
            
        
    
    