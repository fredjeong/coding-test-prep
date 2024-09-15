from collections import deque

N, L = map(int, input().split())

def solution(N, L):
    answer = -1

    while L <= 100:
        start = (1/2) * (2*N/L - L + 1)
        end = start + L - 1
        if start == int(start) and end == int(end):
            if start >= 0 and end >= 0:
                answer = [int(start), int(end)]
                break
    
        L += 1

    return answer

if __name__ == "__main__":
    result = solution(N, L)
    if result == -1:
        print(result)
    else:
        arr = [i for i in range(result[0], result[1]+1)]
        print(" ".join(map(str, arr)))