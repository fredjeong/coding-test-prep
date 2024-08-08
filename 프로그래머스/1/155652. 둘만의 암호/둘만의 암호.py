#def solution(s, skip, index):
#    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#    for i in arr:
#        if i in skip:
#            arr.remove(i)
#    answer = ''
#    for j in range(len(s)):
#        idx = arr.index(s[j])
#        if idx + index < len(s):
#            answer += arr[idx+index]
#        else:
#            answer += arr[(idx + index)%len(arr)]
#    return answer

def solution(s, skip, index):
    # 알파벳 배열 생성 및 skip 문자를 제외
    arr = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    
    answer = ''
    arr_len = len(arr)  # 사용 가능한 알파벳 배열의 길이
    
    for char in s:
        current_index = arr.index(char)  # 현재 문자의 인덱스
        new_index = (current_index + index) % arr_len  # 새로운 인덱스 계산
        answer += arr[new_index]  # 새로운 문자 추가
    
    return answer