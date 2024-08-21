def solution(phone_book): 
    answer = True
    
    dic = {} 
    for nums in phone_book: 
        dic[nums] = 1 
    
    # 2.접두어가 Hash map에 존재하는지 찾기 
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
    
            # 3. 본인 자체일 경우는 제외
            if arr in dic and arr != nums:       
                answer = False
                break
                
    return answer