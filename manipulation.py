str_manip = input("Please input a sentence: ")
input_len = len(str_manip)

# Get the last letter using slice
last_str = str_manip[-1:]
print(f"The lenght of your sentence is: {input_len}")
# Use replace function passing last_str as arg.
replaced_str = str_manip.replace(last_str, "@")
print(replaced_str)
backwards_three = str_manip[input_len - 1:input_len - 4:-1]
print(backwards_three)
five_letter = str_manip[:3] + str_manip[input_len - 2: input_len + 1]
print(five_letter)