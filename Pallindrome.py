# To check string is palindrome

def is_palindrome(string):
    # to remove space in sentence and make it in lowercase
    string = string.replace(" ", "").lower()
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

user_string = input("Enter a string: ")
if is_palindrome(user_string):
    print(f"{user_string} is a Palindrome")
else:
    print(f"{user_string} is not a Palindrome")