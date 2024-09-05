def solution(k, ranges):
    # 우박수열이 1이 될 때까지 정리
    seq = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        seq.append(k)
    n = len(seq)
    # a = 33.3, b = 31.5라면
    # a부터 n-b까지의 정적분을 수행해야 한다
    
    # int(a)부터 int(a+1)까지의 일차함수, n-int(b)-1부터 n-int(b)까지의 일차함수
    # 나머지는 최소 + 최대 * 1/2하면 된다
    # 일차함수: y=(y2-y1)x + y1 - (y2-y1)x1
    # int(a)와 int(a+1)가 만드는 일차함수에 a를 넣고 값을 구하고 그 값과 int(a+1) 사이의 정적분 계산
    answer = []
    for i in ranges:
        a = i[0]
        b = n - 1 + i[1]
        if a == b:
            answer.append(0)
            continue
        if a > b:
            answer.append(-1)
            continue
        # 일차함수: y=(y2-y1)x + y1 - (y2-y1)x1
        if a == int(a):
            part_1 = (seq[int(a)] + seq[int(a+1)]) / 2
        else:
            part_1 = ((seq[int(a+1)]-seq[int(a)]) * a + seq[int(a)] - (seq[int(a+1)] - seq[int(a)])*int(a) + seq[int(a+1)]) * (int(a+1) - a) / 2
        if b == int(b):
            part_2 = (seq[int(b-1)] + seq[int(b)]) / 2
        else:
            part_2 = (seq[int(b)] + ((seq[int(b+1)] - seq[int(b)]) * b + seq[int(b)] - (seq[int(b+1)] - seq[int(b)])*int(b))) * (b - int(b)) / 2
        temp = part_1 + part_2
        if int(a) == int(b) - 1:
            answer.append(part_1)
            continue
        
        for j in range(int(a)+1, int(b)-1):
            temp += (seq[j] + seq[j+1]) / 2
        #print(f"Part 1: {part_1}, Part 2: {part_2}")
        answer.append(temp)
        
    # a == b인 경우, 등 고려
    
    #answer = []
    return answer


