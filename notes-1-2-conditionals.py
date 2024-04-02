# Conditionals 
# Author: Jimmy Cao 
# Date: Feb 14, 2024

# Implement the flowchart from notes 

# create two variables (x and y)
x = 1_000_000
y = -5.2

# if x is less than y, print that 

# if x < y: 
#     print("x is less than y ")
# if x > y:
#     print("x is greater than y")
# if x == y: 
#     print("x equals to y")

if x < y: 
    print("x is less than y ")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# if x is greater than y, print that


# if x is equal to y, print that

# Ask the user what their favorite fruit is 

fave_fruit = input("What's your favorite fruit?")

# If answer apple or orange
if fave_fruit == "apple" or fave_fruit == "orange":
    print("Delicious choice")

# Ask the user how old they are 

user_age = input("How old are  you?")
# if they answer banana and they're two years old
    # Say Bananas are delicious 
if fave_fruit == "bananas" and user_age == "2":
    print("Bananas are delicious")
