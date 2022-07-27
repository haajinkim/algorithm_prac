def solution(n):
    sqrt = n**(1/2)
    # 파이썬에서 제곱근을 구하는 공식 **(1/2)
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    else: return -1