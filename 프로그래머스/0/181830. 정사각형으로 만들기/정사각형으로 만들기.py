def solution(arr):
    rows = len(arr)
    columns = len(arr[0])
    if rows < columns:
        for _ in range(columns - rows):
            arr.append([0 for _ in range(columns)])
    elif rows > columns:
        for i in range(len(arr)):
            for _ in range(rows - columns):
                arr[i].append(0)
    return arr