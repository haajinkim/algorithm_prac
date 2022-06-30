def solution(n): 
    answer = 0
    for i in range(n):
        if i % 1 or i % i == 0:
            answer += i
        
        
    return len(answer)