def solution(numbers):
    answer = ''
    for i in range(0, len(numbers)):
        if "one" in numbers[i:i+3]:
            answer += "1"
        elif "two" in numbers[i:i+3]:
            answer += "2"
        elif "three" in numbers[i:i+5]:
            answer += "3"
        elif "four" in numbers[i:i+4]:
            answer += "4"
        elif "five" in numbers[i:i+4]:
            answer += "5"
        elif "six" in numbers[i:i+3]:
            answer += "6"
        elif "seven" in numbers[i:i+5]:
            answer += "7"
        elif "eight" in numbers[i:i+5]:
            answer += "8"
        elif "nine" in numbers[i:i+4]:
            answer += "9"
        elif "zero" in numbers[i:i+4]:
            answer += "0"
    return int(answer)
