s = input("Enter a string that contains e :-")
def replace_third_fourth_place_of_e(s):
    count = 0
    new_string = ""
    for char in s:
        if char == 'e':
            count+= 1
            if count == 3 or count == 4:
                new_string += 'o'
            else:
                new_string += char
        else:
            new_string += char
    return new_string

print(new_string)

