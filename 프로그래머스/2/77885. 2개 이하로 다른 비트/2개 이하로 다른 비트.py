def solution(numbers):
    answer = []
    
    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'
        
        if number % 2 == 1:
            bin_number[idx+1] = '0'
        
        answer.append(int(''.join(bin_number), 2))
    
    return answer

# 시간 초과
#def solution(numbers):
#    answer = []
#    for number in numbers:
#        binary = "0" * (17 - len(bin(number)[2:])) + bin(number)[2:]
#        while True:
#            counter = 0
#            number += 1
#            new_binary = "0" * (17 - len(bin(number)[2:])) + bin(number)[2:]
#            for i in reversed(range(len(binary))):
#                if new_binary[i] != binary[i]:
#                    counter += 1
#            if counter > 2:
#                continue
#            answer.append(int('0b' + str(int(new_binary)), 2))
#            break
#    return answer