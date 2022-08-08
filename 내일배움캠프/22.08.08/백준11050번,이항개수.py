"""
자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.
"""
from sys import stdin

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n, k = map(int, stdin.readline().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))