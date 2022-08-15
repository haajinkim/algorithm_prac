"""
큰 문제를 작은 문제로 나눌 수 있다.
작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
"""
import time

d = [0] * 50

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

for num in range(5, 40, 10):
    start = time.time()
    res = fibo(num)
    print(res, '-> 러닝타임:', round(time.time() - start, 2), '초')