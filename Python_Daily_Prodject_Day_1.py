# 3 ways to reverse a string in python

def Reverse_a_string_Slice_Notation(word):
    new_word = word[::-1]
    return new_word

def Reverse_a_string_Functon(word):
    new_word = "".join(reversed(word))
    return new_word

def Reverse_a_string_For_Loop(word):
    new_word = ""

    for i in word:
        new_word = i + new_word
    return new_word


print("Check if input is a palindrom")

print("Enter a string of words: ")
word = input()

# Slice Notation
if(word == Reverse_a_string_Slice_Notation(word)):
    print("Thats a Palindrom")
else:
    print("Thats not a Palindrom")

# Function
if(word == Reverse_a_string_Functon(word)):
    print("Thats a Palindrom")
else:
    print("Thats not a palindrom")

# For loop
if(word == Reverse_a_string_For_Loop(word)):
    print("Thats a Palindrom")
else:
    print("Thats not a palindrom")