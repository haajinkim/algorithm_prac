from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        prcie = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if prcie > q:
                break 
        answer.append(sec)