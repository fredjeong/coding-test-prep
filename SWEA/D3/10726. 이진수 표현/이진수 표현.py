T = int(input()) # 테스트 케이스의 개수

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    bin_m = bin(m)[2:] # n을 이진수 변환

    max_length = len(bin(10**8)[2:]) # 최댓값 10**8의 이진수 표현의 길이
    padded_bin_m = "0"*(max_length - len(bin_m)) + bin_m # 길이를 일정하게 맞춤
    
    answer = "ON" # 정답의 디폴트 값 지정
    
    for i in range(max_length-1, max_length-1-n, -1):
        bit = padded_bin_m[i]
        if bit == "0":
            answer = "OFF"
            break
        
    print(f"#{test_case} {answer}")