def find_factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers."
    elif n==0 or n==1:
        return 1
    else:
        factorial = 1
        for i in range(1,n+1):
            factorial *= i
        return factorial
n = int(input("Enter a number to find its factorial: "))
result = find_factorial(n)
print(f"The factorial of {n} is: {result}")