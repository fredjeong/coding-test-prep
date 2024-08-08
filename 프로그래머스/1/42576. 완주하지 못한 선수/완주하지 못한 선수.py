def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i, j in zip(participant, completion):
        if i!=j:
            return i
        
    return participant[-1]
   

#def solution(participant, completion):
#    answer = ''
#    d={i:0 for i in participant}
#    for i in participant:
#        d[i] += 1 #d에 participant의 각 인덱스 별 개수 저장
#    d1={i:0 for i in completion}
#    for i in completion:
#        d1[i] += 1 # d1에 completion의 각 인덱스 별 개수 저장
#    for i in participant:
#        try: # 동명이인 있음
#            if d[i]!=d1[i]:
#                answer += i
#                break
#        except: # 동명이인 없음
#            answer += i
#            break
#    return answer

#def solution(participant, completion):
#    answer = ''
#    participant = sorted(participant)
#    completion = sorted(completion)
#    if completion == []:
#        answer = participant[0]
#    else:
#        for i in range(len(completion)):
#            if participant[i] == completion[i]:
#                if i == len(completion) - 1:
#                    answer = participant[-1]
#            else:
#                answer = participant[i]
#    return answer
    
#    answer = ''
#    # 처음부터 하나씩 찾아보는 방법은 비효율적이다.
#    for i in participant:
#        if participant.count(i) == 1: # i가 동명이인이 아닌 경우
#            if i in completion:
#                #participant.remove(i)
#                #completion.remove(i)
#                pass
#            else:
#                answer = i
#                break
#        else: # i가 동명이인인 경우
#            if participant.count(i) == completion.count(i):
#                #participant.remove(i)
#                #completion.remove(i)
#                pass
#            else:
#                answer = i
#                break
#    return answer
#    #print(answer)
            
#    answer = ''
#    # 한 명은 완주하지 못했다
#    # 동명이인이 있을 수 있다
#    # participant에 있지만 completion에 없는 이름을 찾아야 한다
#    participant = sorted(participant)
#    completion = sorted(completion)
#    while len(completion) != 0:
#        if len(completion) == 1:
#            if completion[0] == participant[0]:
#                answer = participant[1]
#                break
#            else:
#                answer = participant[0]
#                break
#        else:
#            if completion[0] == participant[0]:
#                completion.remove(completion[0])
#                participant.remove(participant[0])
#            else:
#                answer = participant[0]
#                break
#    return answer