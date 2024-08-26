def solution(x, y, n):
    answer = 0
    
    s = set()
    s.add(x)
    
    while s:
        if y in s:
            return answer
        
        new_x = set()
        
        for i in s:
            if i + n <= y:
                new_x.add(i + n)
            
            if i * 2 <= y:
                new_x.add(i * 2)
            
            if i * 3 <= y:
                new_x.add(i * 3)
        
        s = new_x
        answer += 1 
    
    return -1

# 시간 초과
#def solution(x, y, n):
#    global answer
#    answer = -1
#    counter = -1
#    
#    def dfs(current_num, y, n, counter):
#        global answer
#        counter += 1
#        if current_num > y:
#            return
#        elif current_num == y:
#            if answer == -1: 
#                answer = counter
#            else:
#                if counter < answer:
#                    answer = counter
#            return
#
#        temp_1 = current_num + n
#        temp_2 = current_num * 2
#        temp_3 = current_num * 3
#        
#        dfs(temp_1, y, n, counter)
#        dfs(temp_2, y, n, counter)
#        dfs(temp_3, y, n, counter)
#    
#    dfs(x, y, n, counter)
#    
#    return answer