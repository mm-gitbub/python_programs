def print_something(value):
    if value == 'a':
        print("Option One")
        exit()
    elif value == 'b':
        print("Option Two")
    else:
        print("Option Three")
    print("Option Four")
    return(value)
print("Option Five")

# for v in ['a', 'b', 'c']:
# for v in ['b', 'a', 'c']:
# for v in ['c', 'b', 'a']:
for v in ['c', 'a', 'b']:
    result = print_something(v)
    print(result)