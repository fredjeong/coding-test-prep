from itertools import product

def solution(users, emoticons):
    answer = []
    discount = [10, 20, 30, 40]   
    for combi in product(discount, repeat=len(emoticons)):
        service = 0
        revenue = 0
        dic = {} 
        for user in range(len(users)):
            dic[user] = 0

        for i in range(len(combi)):
            for user in range(len(users)):
                if combi[i] >= users[user][0]:
                    dic[user] += int(emoticons[i] * (100 - combi[i]) * 0.01)
        
        for user in range(len(users)):
            if dic[user] >= users[user][1]:
                dic[user] = 0
                service += 1
            else:
                revenue += dic[user]
                
        answer.append([service, revenue])
    
    answer = sorted(answer, reverse=True)
    
    return answer[0]