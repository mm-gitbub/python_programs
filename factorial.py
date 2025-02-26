from main import number_one

factorial = 1
for num in range(1,number_one+1):
    print(num)
    factorial = factorial * num
    print(factorial)
    print("-----------")
print(f'Factorial of a number {number_one} is {factorial}')