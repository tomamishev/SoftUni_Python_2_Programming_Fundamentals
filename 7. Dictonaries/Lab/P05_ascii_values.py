# Write a program that receives a list of characters separated by ", ". It should create a dictionary with each
# character as a key and its ASCII value as a value. Try solving that problem using comprehension.

text = input().split(", ")
ascii_dict = {char: ord(char) for char in text}
print(ascii_dict)