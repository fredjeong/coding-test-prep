def solution(picks, minerals):
    # 광물은 다섯개씩 쪼개서 보자
    arr = []
    stack = []
    for i in range(len(minerals)):
        stack.append(minerals[i])
        if i % 5 == 4 or i == len(minerals)-1:
            arr.append(stack)
            stack = []
    
    # 이 중에서 주어진 곡괭이로 캘 수 있는 것만 보자
    if sum(picks) < len(arr):
        for i in range(len(arr)-sum(picks)):
            arr.pop()
    
    def dfs(picks, arr, pick, tiredness):
        # 캐야 하는 광물이 더 이상 없거나 곡괭이를 다 썼다면 리턴
        if picks[pick] == 0:
            return
        
        # 캐야하는 광물 묶음
        given_arr = arr[0]
        
        # 곡괭이 횟수 차감
        new_picks = picks[:]
        new_picks[pick] -= 1
        
        # 피로도 계산
        if pick == 0:
            for mineral in given_arr:
                tiredness += 1
        elif pick == 1:
            for mineral in given_arr:
                if mineral == 'diamond':
                    tiredness += 5
                else:
                    tiredness += 1
        elif pick == 2:
            for mineral in given_arr:
                if mineral == 'diamond':
                    tiredness += 25
                elif mineral == 'iron':
                    tiredness += 5
                elif mineral == 'stone':
                    tiredness += 1
        
        if len(arr) == 1:
            answer.add(tiredness)
            return
        else:
            temp = arr[1:]
            dfs(new_picks, temp, 0, tiredness)
            dfs(new_picks, temp, 1, tiredness)
            dfs(new_picks, temp, 2, tiredness)
    
    answer = set()
    dfs(picks, arr, 0, 0)
    dfs(picks, arr, 1, 0)
    dfs(picks, arr, 2, 0)
    return min(answer)
#def solution(picks, minerals):
#    answer = []
#    # minerals을 다섯개씩 쪼개서 보자
#    arr = []
#    stack = []
#    
#    for i in range(len(minerals)):
#        stack.append(minerals[i])
#        if i%5 == 4 or i == len(minerals)-1:
#            arr.append(stack)
#            stack = []
#    
#    # 이중에서 주어진 곡괭이로 캘 수 있는 것만 보자
#    if sum(picks) < len(arr):
#        for i in range(len(arr)-sum(picks)):
#            arr.pop()
#    
#    # 남아있는 광물 묶음을 다이아몬드, 철, 돌 곡괭이로 캤을 때의 피로도를 계산하자
#    # 가능한 경우를 dfs로 조사하면 된다
#    def dfs(arr, picks, pick, tiredness):
#        #if arr == []:
#        #    return
#            #return tiredness
#        
#        if pick == 'diamond' and picks[0] == 0:
#            return
#        elif pick == 'iron' and picks[1] == 0:
#            return
#        elif pick == 'stone' and picks[2] == 0:
#            return
#        
#
#        given_arr = arr[0] # 이번에 캐야하는 광물 묶음
#        
#        # 광물 캐고 피로도 계산
#        if pick == 'diamond':
#            for mineral in given_arr:
#                tiredness += 1
#            picks[0] -= 1
#        elif pick == 'iron':
#            for mineral in given_arr:
#                if mineral == 'diamond':
#                    tiredness += 5
#                else:
#                    tiredness += 1
#            picks[1] -= 1
#        elif pick == 'stone':
#            for mineral in given_arr:
#                if mineral == 'diamond':
#                    tiredness += 25
#                elif mineral == 'iron':
#                    tiredness += 5
#                elif mineral == 'stone':
#                    tiredness += 1
#            picks[2] -= 1
#        #print(f"Used {pick} Total Tiredness {tiredness}")
#        #print(tiredness)
#        #print(picks)
#        # 다이아몬드 곡괭이 사용
#        #print(tiredness)
#        if arr == 1:
#            return
#        else:
#            arr.pop(0)
#            dfs(arr, picks, 'diamond', tiredness)
#            # 철 곡괭이 사용
#            dfs(arr, picks, 'iron', tiredness)
#            # 돌 곡괭이 사용
#            dfs(arr, picks, 'stone', tiredness)
#    
#    #diamond = dfs(arr=arr, picks=picks, pick='diamond', tiredness=0)
#    #answer = []
#    
#    dfs(arr, picks=picks, pick='diamond', tiredness=0)
#    #dfs(arr, picks=picks, pick='iron', tiredness=0)
#    #dfs(arr, picks=picks, pick='stone', tiredness=0)
#    #print(answer)
#
#    #stone = dfs(arr, picks=picks, pick='stone', tiredness=0)
#    
##    answer = 0
##    return answer