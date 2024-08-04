def solution(quiz):
    answer = []
   
    for i in quiz :
    	
        #'='를 기준으로 분리 
        xy , z = i.split('=')[0] , i.split('=')[1]
        #계산하기위해 x와 y 분리하기 
        x , oper , y = xy.split()[0] , xy.split()[1] , xy.split()[2]
        
        #int형으로 변환 
        x , y, z = int(x) , int(y) , int(z)
    	
        #만일 연산자에 따른 계산 
        if oper == '+' :
            result = x+y 
        else :
            result = x-y 
		
        #만일 계산결과와 z 가 동일하다면 O, 아니라면 X 
        if result == z : 
            answer.append("O")
        else :
            answer.append("X")
    
    return answer