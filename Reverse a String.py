# Program to reverse a string


# with indexing
def rev_string_with_indexing(user_string):
    rev_user_string = user_string[::-1]
    return rev_user_string

# without indexing
def rev_string_without_indexing(user_string):
    reversed_string = ""
    for s in user_string:
        reversed_string = reversed_string + s

    return reversed_string


# user input
input_string = input("Enter a string: ")
print(f"Reversed string using indexing: {rev_string_with_indexing(input_string)}")
print(f"Reversed string without using indexing: {rev_string_without_indexing(input_string)}")

