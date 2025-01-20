T = int(input())

for test_case in range(1, T+1):
    vowels = {"a", "e", "i", "o", "u"}
    ans = ""
    s = input().strip()
    for char in s:
        if char not in vowels:
            ans += char

    print(f"#{test_case} {ans}")