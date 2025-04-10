from main import number_one

def febonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return febonacci(n-1) + febonacci(n-2)

result = febonacci(number_one)
print(f"The febonacci series of the number '{number_one}' is {result}")
