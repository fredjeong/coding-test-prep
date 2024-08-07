def solution(s, n):
    answer = ''
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in s:
        # 공백인지 문자인지 확인
        if i != ' ':
            # 인덱싱 위해서 소문자 변환
            temp = i.lower()

            # 나머지 이용해서 밀어내기
            index = arr.index(temp)
            step = n%len(arr)

            # 한바퀴 이상 도는지 확인
            if index + step >= len(arr):
                new = arr[index + step - len(arr)]
            else:  
                new = arr[index + step]
            
            # 대소문자 판별해서 답안 리스트에 추가
            if i == temp: 
                answer += new
            else: 
                answer += new.upper()
        else:
            answer += i
    return answer