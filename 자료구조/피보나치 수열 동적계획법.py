input = 100

# 1. 메모용 데이터를 만든다 처음 값인 Fibo(1).Fibo(2)는 각각 1씩 넣어서 저장해준다.
# 2. Fibo(n) 을 구할 때 만약 메모에 그 값이 있다면 바로 반환한다.
# 3. Fibo(n) 을 처음 구했다면 메모에 그 값을 기억한다

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    # 구현해보세요!
    if n in fibo_memo:
        return fibo_memo[n]
    
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n -2 , fibo_memo) 
    fibo_memo[n] = nth_fibo
    
    return nth_fibo


print(fibo_dynamic_programming(input, memo))