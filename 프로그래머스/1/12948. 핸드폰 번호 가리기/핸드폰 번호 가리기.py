def solution(phone_number):
    asterisk = "*" * (len(phone_number)-4)
    answer = asterisk + phone_number[-4:]
    #answer = phone_number
    #if len(phone_number) != 4:
    #    for i in range(len(phone_number)-4):
    #        answer = answer.replace(answer[i], "*")
    #else:
    #    answer = phone_number
    #        
    #
    return answer