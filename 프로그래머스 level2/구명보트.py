from collections import deque
def solution(people, limit):
    people.sort()
    queue = deque(people)
    boat = 0

    while queue:
        if len(queue) >= 2:
            if queue[0] + queue[-1] <= limit:
                queue.pop()
                queue.popleft()
                boat +=1
            elif queue[0] + queue[-1] >= limit:
                queue.pop()
                boat +=1
        else:
            if queue[0] <= limit:
                queue.pop()
                boat += 1
    
    return boat