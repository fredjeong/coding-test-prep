string = str(input())

def solution(string):
    length = len(string)
    if length == 1:
        return 1

    # 홀수인 경우
    if length%2 == 1:
        for i in range(int(length//2), length):
            if i == length-1:
                return length + length-1
            attach_length = length - i - 1
            if string[i+1:][::-1] == string[i-attach_length:i]:
                return length + i - attach_length

            elif string[i+1:][::-1] == string[i-attach_length+1:i+1]:
                return length + i + 1 - attach_length
    # 짝수인 경우
    else:
        for i in range(int(length//2)-1, length):
            if i == length-1:
                return length + length-1
            attach_length = length - i - 1
            if string[i+1:][::-1] == string[i-attach_length:i]:
                return length + i - attach_length

            elif string[i+1:][::-1] == string[i-attach_length+1:i+1]:
                return length + i + 1 - attach_length

if __name__ == '__main__':
    result = solution(string)
    print(result)