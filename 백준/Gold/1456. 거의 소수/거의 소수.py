import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def get_primes(num):
    arr = [False for _ in range(num+1)]
    arr[0] = True
    arr[1] = True
    for i in range(2, int(num**0.5)+1):
        for j in range(2*i, num+1, i):
            arr[j] = True
    new_arr = [i for i in range(len(arr)) if not arr[i]]
    return new_arr

arr = get_primes(int(b**0.5))

s = set()
for num in arr:
    new_num = num**2
    while new_num <= b:
        if new_num >= a:
            s.add(new_num)
        new_num *= num

print(len(s))