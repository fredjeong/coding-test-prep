from itertools import product

def solution(users, emoticons):
    # 목표 1: 이모티콘 플러스 서비스 가입자 최대한 늘리기
    # 목표 2: 이모티콘 판매액을 최대한 늘리기
    
    # 각 이모티콘마다 할인율을 적절하게 설정하여
    # 각 사용자들이 구매하는 이모티콘의 총합이 users[i][1] 이상 되도록 만들어야 한다
    # 이모티콘은 총 7종류이므로 완전탐색이 가능할지도?
    # 할인율은 10, 20, 30, 40 중 하나로 설정된다
    # 그러므로 총 4**7개의 조합이 가능해진다 -> 16384개이므로 완전탐색 가능
    
    # 각 조합에 대하여 사용자들의 소비액이 기준 가격을 넘는지 보고, 
    # 기준 가격을 초과하면 이모티콘 플러스 서비스 가입 여부에 +1, 
    # 아니라면 이모티콘 구매 비용을 총 매출애 산입한다. 
    # 각 조합에 대하여 이렇게 나온 결과물 (서비스 가입 여부, 구매 비용)을 리스트에 추가하고,
    # 리스트를 sorted한다.
    
    answer = []
    # Step 1: 이모티콘별 할인율 정하기
    discount = [10, 20, 30, 40]   
    #data = list(product(discount, repeat = 7))
    for combi in product(discount, repeat=len(emoticons)):
        #combi = list(combi)
        service = 0
        revenue = 0
        dic = {} 
        for user in range(len(users)):
            dic[user] = 0

        # i번째 이모티콘
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