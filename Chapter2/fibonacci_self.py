fibonacci_list = {1: 1, 2: 1}

def fibonacci(n):
    if n in fibonacci_list:
        return fibonacci_list[n]
    
    fibonacci_list[n] = fibonacci(n - 2) + fibonacci(n -1)
    return fibonacci_list[n]

print(fibonacci(50))