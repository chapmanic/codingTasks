# Part 1 Alternative Char ----------------------------------
user_string = input("Please provide a word or sentence: ")
list_capital = [letter.upper() if i % 2 == 0 else letter.lower() for i, letter in enumerate(user_string)]
print(''.join(list_capital))


# Part 2 Alternative word -----------------------------------
# Create a variable which takes the users sentence and splits each word into a list, using the .split function with " " as the delimiter 
separated_list = user_string.split(" ")
# Used same list comprehension as part 1. However, used NOT to alterative the capitalization 
capital_word = [word.upper() if not i % 2 == 0 else word.lower() for i, word in enumerate(separated_list)]
# Used join() with " " as separator 
print(" ".join(capital_word))