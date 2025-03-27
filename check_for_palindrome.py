#from main import number_one
word = "mom"
def ispalindrom(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and ispalindrom(s[1:-1])
result = ispalindrom(word)
print(f"The word is palindrome")

