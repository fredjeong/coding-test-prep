import sys
N = int(input())
arr = list(map(int, input().split()))

# N명의 키가 모두 다르다

# 자기 앞에 자기보다 키 큰 사람 몇 명이 있었는지를 나타낸다
"""
1번 난쟁이는 arr[1-1] 인덱스에 위치한다 (이건 고정)
다음으로 2번 난쟁이를 보자
2번 난쟁이가 갈 수 있는 인덱스는 arr[1-1] 또는 arr[1-1]+1(자기보다 키 작은 사람 수)
3번 난쟁이가 갈 수 있는 인덱스는 arr[2-1] 또는 arr[2-1]+2
아니면 arr[2-1], arr[2-1]+1, arr[2-1]+2를 모두 고려?
남는 곳에 마지막 난쟁이가 간다
"""
# arr = [2, 1, 1, 0]이라면
# 1번 난쟁이 앞에는 두 명의 사람이 왔다
# 따라서 1번 난쟁이의 위치는 3번이다

# 2번 난쟁이 앞에는 한 명의 사람이 왔다
# 따라서 2번 난쟁이의 위치는 1번이다
# 4 2 1 3

def solution(N, arr):
    line = [0 for _ in range(N)]
    #line[arr[0]] = 1 # 1번 지정
    global answer
    answer = 0
    def dfs(N, arr, line, num, idx):
        global answer
        temp = line[:] # 깊은 복사

        if temp[idx] != 0:
            return
        
        if num == N:
            temp[temp.index(0)] = num
            # 정확도 체크
            for i in range(1, N+1):
                id = temp.index(i)
                count = 0
                for rand in temp[:id]:
                    if rand > i:
                        count += 1
                if count != arr[i-1]:
                    return

            answer = temp
            return
            #else:
            #    return
            #for i in range(N):
            #    if temp[i] == 0:
            #        temp[i] = num
            #        answer = temp
            #        return

        temp[idx] = num
        
        #print(arr[num])
        #print(arr[num]+num)
        
        #for k in range(num+1):
        #    dfs(N, arr, temp, num+1, arr[num]+k)
        j = 0
        while j <= num:
            dfs(N, arr, temp, num+1, arr[num]+j)
            j += 1 
        #dfs(N, arr, temp, num+1, arr[num])
        #dfs(N, arr, temp, num+1, arr[num]+num)

    dfs(N, arr, line, 1, arr[0])

    return answer

if __name__ == "__main__":
    result = solution(N, arr)
    print(" ".join(map(str, result)))
#q = deque()
#q.append(1)
#
#while q:
#    num = q.popleft()
#    
#    for arr[
#    # 갈 수 있는 위치 선정하고
#    # 거기에 맞게





