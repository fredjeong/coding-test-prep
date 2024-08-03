def solution(numbers, direction):
    if direction == 'right':
        answer = [numbers[-1]] + numbers[:-1]
    else:
        answer = numbers[1:] + [numbers[0]]
    return answer