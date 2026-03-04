import re

# Task 6
# Replace all spaces, commas and dots with colon

# Regex: [ ,.]

text = input("Enter text: ")
#Hello, world. Python regex

# Explanation:
# [ ,.] -> matches space, comma or dot
matches = re.findall(r"a.*b", text)

print(matches)