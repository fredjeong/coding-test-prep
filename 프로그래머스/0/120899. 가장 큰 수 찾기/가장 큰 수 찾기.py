def solution(array):
    new_array = sorted(array)
    largest = new_array[-1]
    index = array.index(largest)
    return [largest, index]