def solution(s):
    s = s.lstrip('{{')
    s = s.rstrip('}}')
    s = s.split("},{")
    
    for i in range(len(s)):
        s[i] = s[i].split(",")
        for j in range(len(s[i])):
            s[i][j] = int(s[i][j])
    
    s = sorted(s, key=lambda x: len(x))        
    
    arr = s[0]
    for i in range(1, len(s)):
        arr += [j for j in s[i] if j not in s[i-1]]
    
    return arr