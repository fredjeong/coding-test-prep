N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def calculate_area(A, B, C):
    area = abs((A[0]*B[1] + B[0]*C[1] + C[0]*A[1]) - (B[0]*A[1] + C[0]*B[1] + A[0]*C[1]))*0.5
    return area

def solution(N, arr):
    if N == 3:
        return calculate_area(arr[0], arr[1], arr[2])
    
    answer = 0
    for i in range(N-2):
        A = arr[i]
        temp = arr[i+1:]
        for j in range(N-i-1):
            B = temp[j]
            temp_2 = temp[j+1:]
            for elem in temp_2:
                C = elem
                area = calculate_area(A, B, C)
                if area > answer:
                    answer = area
    return answer

if __name__ == '__main__':
    result = solution(N, arr)
    print(result)