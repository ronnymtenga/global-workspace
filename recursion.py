def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)

def fibonacci(x):
    if x==0:
        return 0
    if x==1:
        return 1
    return fibonacci(x-1)+fibonacci(x-2)

for i in range(10): print(fibonacci(i))