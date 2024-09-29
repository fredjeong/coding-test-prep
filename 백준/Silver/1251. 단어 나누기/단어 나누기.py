import sys

input = sys.stdin.readline

string = input().strip()


if len(string) in [1, 2, 3]:
    print(string)
else:
    result = []
    idx_1, idx_2 = 1, 2
    for idx_1 in range(1, len(string)-1):
        for idx_2 in range(idx_1+1, len(string)):
            temp_1 = string[:idx_1]
            temp_1 = temp_1[::-1]
            temp_2 = string[idx_1:idx_2]
            temp_2 = temp_2[::-1]
            temp_3 = string[idx_2:]
            temp_3 = temp_3[::-1]
            temp = temp_1 + temp_2 + temp_3
            result.append(temp)
    result.sort()
    print(result[0])