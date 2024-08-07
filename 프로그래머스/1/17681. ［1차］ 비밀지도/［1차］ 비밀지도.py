def solution(n, arr1, arr2):
    answer = ["" for i in range(n)]

    for i in range(len(arr1)):
        # 주어진 수를 이진법으로 변경
        i_bin_1 = bin(arr1[i])
        i_bin_2 = bin(arr2[i])
        
        # 이진법에서 앞 두 글자 "0b" 제거
        i_bin_1 = i_bin_1[2:]
        i_bin_2 = i_bin_2[2:]
        
        # 이진법 문자열의 길이가 n 미만일 경우 "n-이진법 문자열 길이"만큼 0 추가
        if len(i_bin_1) < n:
            i_bin_1 = "0"*(n - len(i_bin_1)) + i_bin_1
        if len(i_bin_2) < n:
            i_bin_2 = "0"*(n - len(i_bin_2)) + i_bin_2
        
        # arr1, arr2 다시 설정 (이진법 문자열로)
        arr1[i] = i_bin_1
        arr2[i] = i_bin_2
    
    # 두 배열 모두에 대해서 arr1[i][j]과 arr2[i][j] 비교
    for i in range(n):
        for j in range(n):
            # arr[i][j] == 1 or arr[i][j] == 1일 경우 answer.append("#") 아닐 경우 answer.append(" ")
            if arr1[i][j] == "1" or arr2[i][j] == "1":
                answer[i] += "#"
            else:
                answer[i] += " "
    
    return answer