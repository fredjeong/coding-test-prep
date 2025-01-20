T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    
    mean = sum(arr) // n
    for num in arr:
        if num <= mean:
            ans += 1
            
    print(f"#{test_case} {ans}")