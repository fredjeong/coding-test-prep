import sys
A, K = map(int, input().split())

from collections import deque

def solution(A, K):
    count = 0

    while A < K:
        if K % 2 == 0 and K // 2 >= A:
            K //= 2
        else:
            K -= 1
    
        count += 1               
                    
    return count


if __name__ == '__main__':
    result = solution(A, K)
    print(result)