def solution(phone_book): 
    answer = True
    
    dic = {} 
    for nums in phone_book: 
        dic[nums] = 1 
    
    for number in phone_book: 
        arr = "" 
        for num in number: 
            arr += num
            if arr in dic and arr != number:       
                answer = False
                break
                
    return answer