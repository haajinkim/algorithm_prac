from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for permut in permutations(dungeons, len(dungeons)):
        hp = k
        count = 0
        for pm in permut:
            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
        if count > answer:
            answer = count
    
    return answer

