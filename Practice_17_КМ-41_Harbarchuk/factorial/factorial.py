def fact(x):
    factorial = 1
    for i in range(1, x+1):
        factorial = factorial * i
    
    return factorial