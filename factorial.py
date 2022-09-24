def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result* x
    return result

for n in range(1,10):
    print(n, factorial(n))