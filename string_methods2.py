# 2.3 - String Methods 2 - Jon Tokarz - June 29, 2024


# Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
capitalized_string1 = string1.capitalize()
print(capitalized_string1)

# Use the center() method to center the string in a string of specified width
# Example: "python" -> " python "
string2 = "python"
centered_string2 = string2.center(9)
print(centered_string2)

# Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
ends_with_on = string3.endswith("on")
print(ends_with_on)

# Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
position_th = string4.find("th")
print(position_th)

# Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
is_alphanumeric = string5.isalnum()
print(is_alphanumeric)

# Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
is_alpha = string6.isalpha()
print(is_alpha)

# Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
is_lower = string7.islower()
print(is_lower)

# Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if " " is all whitespace
string8 = " "
is_whitespace = string8.isspace()
print(is_whitespace)

# Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
is_upper = string9.isupper()
print(is_upper)

# Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
joined_string = separator.join(iterable1)
print(joined_string)

# Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "PYTHON"
lowercase_string10 = string10.lower()
print(lowercase_string10)

# Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from " python"
string11 = " python"
stripped_string11 = string11.lstrip()
print(stripped_string11)

# Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python "
string12 = "python "
stripped_string12 = string12.rstrip()
print(stripped_string12)

# Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
replaced_string13 = string13.replace("python", "snake")
print(replaced_string13)

# Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
highest_index_n = string14.rfind("n")
print(highest_index_n)

# Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
split_list = string15.split("-")
print(split_list)

# Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
starts_with_py = string16.startswith("py")
print(starts_with_py)

# Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from " python "
string17 = " python "
stripped_string17 = string17.strip()
print(stripped_string17)

# Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
swapped_case_string18 = string18.swapcase()
print(swapped_case_string18)

# Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
title_case_string19 = string19.title()
print(title_case_string19)

# Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
uppercase_string20 = string20.upper()
print(uppercase_string20)



# 2.3 - String Methods 2 - Jon Tokarz - June 29, 2024