"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
"""

m,n= map(int, input().split())
def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)
        
def lcd(m,n):
    return m*n // gcd(m,n) 

print(gcd(m,n))
print(lcd(m,n))
