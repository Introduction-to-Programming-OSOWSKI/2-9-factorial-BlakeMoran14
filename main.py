#WRITE YOUR CODE IN THIS FILE

def factorial(x):
    for i in range(1, x):
        x = x * i

    return x

print(factorial(10))