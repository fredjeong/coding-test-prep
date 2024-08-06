def solution(s):
    # 변환된 단어를 저장하는 리스트
    arr = []
    
    # 공백을 기준으로 단어 분리하여 리스트 생성
    s = s.split(" ")
    
    # for문 두 개로 새 문자열 생성하여 리스트에 추가
    for i in range(len(s)):
        temp = ''
        for j in range(len(s[i])):
            if j%2 == 0:
                temp += s[i][j].upper()
            else:
                temp += s[i][j].lower()
        arr.append(temp)
    
    # 리스트 합치기
    answer = ''
    for i in arr:
        answer += ' ' + i 
    answer = answer[1:]
    
    return answer