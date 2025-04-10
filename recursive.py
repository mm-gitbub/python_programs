from main import number_one

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

result = factorial(number_one)
print(result)
