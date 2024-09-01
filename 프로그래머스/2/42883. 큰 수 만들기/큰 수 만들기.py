def solution(number, k):
    answer = []
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])

#def solution(number, k):
#    answer = ""
#    length = len(number) - k
#    temp = str(number[0])
#    
#    for i in range(1, len(number)):
#        if len(temp) < length:
#            temp += str(number[i])
#        else:
#            min_index = temp.index(min(temp))
#            if min_index == len(temp) - 1:
#                if temp[-1] <= str(number[i]):
#                    temp = temp[:min_index] + str(number[i])
#            else:
#                if temp[min_index] < temp[min_index + 1]:
#                    temp = temp[:min_index] + temp[min_index+1:] + str(number[i])
#                else:
#                    pass
#    
#    return temp