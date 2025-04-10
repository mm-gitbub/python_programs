from main import number_two

print(f"The original number is {number_two}")
def sum_of_the_number(n):
    if n < 10:
        return n
    else:
        all_but_last = n//10
        last = n % 10
        return last + sum_of_the_number(all_but_last)

result = sum_of_the_number(number_two)
print(f"The sum of the original number is {result}")
