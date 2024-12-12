import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer

if arr[0] == 1:
    k = arr[1] - 1
    nums = list(range(1, n+1))
    answer = []

    while n > 0:
        facto = factorial(n-1)
        digit = k // facto
        k %= facto
        n -= 1
        answer.append(nums[digit])
        del nums[digit]
    answer += nums
    print(' '.join(map(str, answer)))

else:
    arr = arr[1:]

    answer = 0

    for i in range(n):
        sorted_arr = sorted(arr)
        ranks = [sorted_arr.index(j) for j in arr]
        answer += ranks[0] * factorial(n-1-i)
        arr = arr[1:]
    print(answer+1)