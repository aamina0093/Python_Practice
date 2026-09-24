# program to count vowels in a string

def count_vowels(string):
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        if vowel in string:
            print(vowel)
            vowel_count += 1
    return vowel_count



# user input
user_string = input("Enter a string: ")
print(f"The number of vowels in {user_string} is {count_vowels(user_string)}")