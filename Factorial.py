# factorial with recursion

def factorial_with_recursion(number):
    if number == 0:
        return 1
    else:
        return number * factorial_with_recursion(number - 1)

def factorial_without_recursion(number):
    if number == 0:
        return 1
    else:
        factorial = 1
        while (number > 1):
            factorial *= number
            number -= 1

        return factorial

# user_input
user_number = int(input("Enter a number: "))
print(f"Factorial of {user_number} with recursion is {factorial_with_recursion(user_number)}")
print(f"Factorial of {user_number} without recursion is {factorial_without_recursion(user_number)}")


