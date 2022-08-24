

n = int(input())

if n % 4 == 0 and n % 100 >= 1 :
    n = 1
elif n % 400 == 0:
    n = 1
else:
    n = 2
print(n)